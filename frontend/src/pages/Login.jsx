import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Login = () => {

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const navigate = useNavigate();

  const handleLogin = async (e) => {

    e.preventDefault();

    try {

      const response = await axios.post(
        "http://localhost:8000/api/login",
        {
          email: email,
          password: password
        }
      );

      const token = response.data.token;

      localStorage.setItem("token", token);

      navigate("/dashboard");

    } catch (err) {

      setError("Invalid credentials");

    }

  };

  return (

    <div style={{ width: "300px", margin: "100px auto" }}>

      <h2>InsightFlow Login</h2>

      <form onSubmit={handleLogin}>

        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          style={{ display: "block", marginBottom: "10px", width: "100%" }}
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={{ display: "block", marginBottom: "10px", width: "100%" }}
        />

        <button type="submit">Login</button>

      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}

    </div>

  );

};

export default Login;