import React, { createContext, useState, useEffect } from "react";
import { loginUser, logoutUser, isAuthenticated } from "../services/auth";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {

  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);


  useEffect(() => {

    const checkAuth = () => {

      if (isAuthenticated()) {
        setUser({ authenticated: true });
      } else {
        setUser(null);
      }

      setLoading(false);

    };

    checkAuth();

  }, []);


  const login = async (email, password) => {

    try {

      const data = await loginUser(email, password);

      setUser(data.user || { authenticated: true });

      return { success: true };

    } catch (error) {

      return {
        success: false,
        message: error.response?.data?.detail || "Login failed"
      };

    }

  };


  const logout = () => {

    logoutUser();

    setUser(null);

  };


  return (

    <AuthContext.Provider
      value={{
        user,
        loading,
        login,
        logout
      }}
    >

      {children}

    </AuthContext.Provider>

  );

};