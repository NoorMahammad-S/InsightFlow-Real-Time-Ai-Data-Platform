import React, { useContext } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Upload from "./pages/Upload";

import { AuthProvider, AuthContext } from "./context/AuthContext";



const PrivateRoute = ({ children }) => {

  const { user, loading } = useContext(AuthContext);

  if (loading) return <div>Loading...</div>;

  return user ? children : <Navigate to="/" />;

};



const AppRoutes = () => {

  return (

    <Routes>

      <Route path="/" element={<Login />} />

      <Route
        path="/dashboard"
        element={
          <PrivateRoute>
            <Dashboard />
          </PrivateRoute>
        }
      />

      <Route
        path="/upload"
        element={
          <PrivateRoute>
            <Upload />
          </PrivateRoute>
        }
      />

    </Routes>

  );

};



function App() {

  return (

    <AuthProvider>

      <Router>

        <AppRoutes />

      </Router>

    </AuthProvider>

  );

}

export default App;