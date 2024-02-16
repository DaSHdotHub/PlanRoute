import axios from "axios";
import { useAuthStore } from "./stores/auth"; // Update the path as necessary to import your Pinia store
const VUE_APP_API_BASE_URL = process.env.VUE_APP_API_BASE_URL;

// Create an Axios instance
const apiClient = axios.create({
  baseURL: VUE_APP_API_BASE_URL,
  timeout: 10000,
});

// Add a request interceptor
apiClient.interceptors.request.use(
  (config) => {
    const authStore = useAuthStore(); // Use the Pinia store
    const token = authStore.token; // Access the token from the Pinia store
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor to handle token refresh logic globally
apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response.status === 401 && !error.config._retry) {
      // If 401 is received, try refreshing the token and retrying the request once
      const authStore = useAuthStore();
      error.config._retry = true;

      await authStore.refreshToken(); 

      error.config.headers.Authorization = `Bearer ${authStore.token}`;
      return apiClient(error.config);
    }
    return Promise.reject(error);
  }
);

export default apiClient;
