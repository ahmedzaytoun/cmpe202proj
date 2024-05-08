import React from "react"
import ReactDOM from "react-dom/client"
import { RouterProvider } from "react-router-dom"
import router from "./router"
import { ChakraProvider, ColorModeScript } from "@chakra-ui/react"
import theme from "./theme"
import { QueryClient, QueryClientProvider } from "@tanstack/react-query"
import { AuthProvider } from "./auth/AuthProvider"
const client = new QueryClient()

const root = ReactDOM.createRoot(document.getElementById("root") as HTMLElement)
root.render(
    <React.StrictMode>
        <QueryClientProvider client={client}>
            <ChakraProvider theme={theme}>
                <ColorModeScript
                    initialColorMode={theme.config.initialColorMode}
                />
                <AuthProvider>
                    <RouterProvider router={router} />
                </AuthProvider>
            </ChakraProvider>
        </QueryClientProvider>
    </React.StrictMode>
)
