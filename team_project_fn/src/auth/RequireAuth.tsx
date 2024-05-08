// src/auth/RequireAuth.tsx

import React, { ReactNode } from "react"
import { Navigate, useLocation } from "react-router-dom"
import { useAuth } from "./AuthProvider"

type Props = {
    children: ReactNode
    role?: string
}

const RequireAuth = ({ children, role }: Props) => {
    const auth = useAuth()
    const location = useLocation()

    if (!auth.user) {
        return <Navigate to="/login" state={{ from: location }} replace />
    } else if (role && auth.user.role !== role) {
        return <Navigate to="/unauthorized" replace />
    }

    return <>{children}</>
}

export default RequireAuth
