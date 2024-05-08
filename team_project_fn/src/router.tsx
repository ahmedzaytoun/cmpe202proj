import { createBrowserRouter } from "react-router-dom"
import Student from "./routes/Student"
import Root from "./components/Root"
const router = createBrowserRouter([
    {
        path: "/",
        element: <Root />,
    },
    {
        path: "/student",
        element: <Student />,
    },
])

export default router
