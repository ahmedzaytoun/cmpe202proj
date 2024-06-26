import { FaMoon, FaSun } from "react-icons/fa"
import { SiCanvas } from "react-icons/si"
import {
    Box,
    Button,
    HStack,
    IconButton,
    useDisclosure,
    useColorMode,
    useColorModeValue,
    Stack,
    Avatar,
    Menu,
    MenuButton,
    MenuItem,
    MenuList,
    useToast,
} from "@chakra-ui/react"
import { Link } from "react-router-dom"
import LoginModal from "./LoginModal"
import useUser from "../lib/useUser"
import { logOut } from "../api"
import { useQueryClient } from "@tanstack/react-query"

export default function Header() {
    const { userLoading, isLoggedIn, user } = useUser()
    const {
        isOpen: isLoginOpen,
        onClose: onLoginClose,
        onOpen: onLoginOpen,
    } = useDisclosure()

    const { toggleColorMode } = useColorMode()
    const logoColor = useColorModeValue("red.500", "red.200")
    const Icon = useColorModeValue(FaMoon, FaSun)
    const toast = useToast()
    const queryClient = useQueryClient()
    const onLogOut = async () => {
        const toastId = toast({
            title: "Login out...",
            description: "Sad to see you go...",
            status: "loading",
            position: "bottom-right",
        })
        await logOut()
        queryClient.refetchQueries({ queryKey: ["me"] })
        toast.update(toastId, {
            status: "success",
            title: "Done!",
            description: "See you later!",
        })
    }
    return (
        <Stack
            justifyContent={"space-between"}
            py={5}
            px={40}
            alignItems="center"
            direction={{
                sm: "column",
                md: "row",
            }}
            spacing={{
                sm: 4,
                md: 0,
            }}
            borderBottomWidth={1}
        >
            <Box color={logoColor}>
                <Link to={"/"}>
                    <SiCanvas size={"48"} />
                </Link>
            </Box>
            <HStack spacing={2}>
                <IconButton
                    onClick={toggleColorMode}
                    variant={"ghost"}
                    aria-label="Toggle dark mode"
                    icon={<Icon />}
                />
                {!userLoading ? (
                    !isLoggedIn ? (
                        <>
                            <Button onClick={onLoginOpen}>Log in</Button>
                        </>
                    ) : (
                        <Menu>
                            <MenuButton>
                                <Avatar
                                    name={user?.name}
                                    src={user?.avatar}
                                    size={"md"}
                                />
                            </MenuButton>
                            <MenuList>
                                <MenuItem onClick={onLogOut}>Log out</MenuItem>
                            </MenuList>
                        </Menu>
                    )
                ) : null}
            </HStack>
            <LoginModal isOpen={isLoginOpen} onClose={onLoginClose} />
        </Stack>
    )
}
