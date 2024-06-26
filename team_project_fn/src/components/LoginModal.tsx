import { useForm } from "react-hook-form"
import {
    Box,
    Button,
    Input,
    InputGroup,
    InputLeftElement,
    Modal,
    ModalBody,
    ModalCloseButton,
    ModalContent,
    ModalHeader,
    ModalOverlay,
    VStack,
    useToast,
} from "@chakra-ui/react"
import { FaUserNinja, FaLock } from "react-icons/fa"

import { useMutation, useQueryClient } from "@tanstack/react-query"
import { usernameLogIn } from "../api"
interface LoginModalProps {
    isOpen: boolean
    onClose: () => void
}
interface IForm {
    username: string
    password: string
}

export default function LoginModal({ isOpen, onClose }: LoginModalProps) {
    const {
        register,
        handleSubmit,
        formState: { errors },
        watch,
    } = useForm<IForm>()
    console.log(watch())
    const toast = useToast()
    const queryClient = useQueryClient()
    const mutation = useMutation({
        mutationFn: usernameLogIn,
        onSuccess: (data) => {
            toast({
                title: "welcome",
                status: "success",
            })
            onClose()
            queryClient.refetchQueries({ queryKey: ["me"] })
        },
        onError: (error) => {
            console.log("mutation error")
        },
    })
    const onSubmit = ({ username, password }: IForm) => {
        mutation.mutate({ username, password })
    }
    return (
        <Modal onClose={onClose} isOpen={isOpen}>
            <ModalOverlay />
            <ModalContent>
                <ModalHeader>Log in</ModalHeader>
                <ModalCloseButton />
                <ModalBody as="form" onSubmit={handleSubmit(onSubmit)}>
                    <VStack>
                        <InputGroup size={"md"}>
                            <InputLeftElement
                                children={
                                    <Box color="gray.500">
                                        <FaUserNinja />
                                    </Box>
                                }
                            />
                            <Input
                                isInvalid={Boolean(errors.username?.message)}
                                {...register("username", {
                                    required: "Please write a username",
                                })}
                                variant={"filled"}
                                placeholder="Username"
                            />
                        </InputGroup>
                        <InputGroup>
                            <InputLeftElement
                                children={
                                    <Box color="gray.500">
                                        <FaLock />
                                    </Box>
                                }
                            />
                            <Input
                                isInvalid={Boolean(errors.password?.message)}
                                {...register("password", {
                                    required: "Please write a password",
                                })}
                                type="password"
                                variant={"filled"}
                                placeholder="Password"
                            />
                        </InputGroup>
                    </VStack>
                    <Button
                        isLoading={mutation.isPending}
                        type="submit"
                        mt={4}
                        colorScheme={"red"}
                        w="100%"
                    >
                        Log in
                    </Button>
                </ModalBody>
            </ModalContent>
        </Modal>
    )
}
