import axios from "axios";

const API_BASE_URL = "http://localhost:8000/api";

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json"
  }
});


// Attach token to every request
api.interceptors.request.use(
  (config) => {

    const token = localStorage.getItem("token");

    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }

    return config;
  },
  (error) => Promise.reject(error)
);


// Dashboard analytics data
export const getDashboardData = async (filters = {}) => {

  const response = await api.get("/dashboard", {
    params: filters
  });

  return response.data;
};


// Dataset upload
export const uploadDataset = async (file) => {

  const formData = new FormData();

  formData.append("file", file);

  const response = await api.post("/dataset/upload", formData, {
    headers: {
      "Content-Type": "multipart/form-data"
    }
  });

  return response.data;
};


// Monitoring metrics
export const getMonitoringMetrics = async () => {

  const response = await api.get("/monitoring");

  return response.data;
};


export default api;