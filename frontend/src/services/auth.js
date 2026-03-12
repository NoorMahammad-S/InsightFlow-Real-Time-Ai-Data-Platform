import axios from "axios";

const AUTH_API = "http://localhost:8000/api/auth";


// Login user
export const loginUser = async (email, password) => {

  const response = await axios.post(`${AUTH_API}/login`, {
    email,
    password
  });

  const token = response.data.token;

  if (token) {
    localStorage.setItem("token", token);
  }

  return response.data;
};


// Register user
export const registerUser = async (userData) => {

  const response = await axios.post(`${AUTH_API}/register`, userData);

  return response.data;
};


// Logout user
export const logoutUser = () => {

  localStorage.removeItem("token");

};


// Get stored token
export const getToken = () => {

  return localStorage.getItem("token");

};


// Check authentication
export const isAuthenticated = () => {

  const token = getToken();

  return !!token;

};