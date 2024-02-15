import axios from 'axios';
import store from './store';
const VUE_APP_API_BASE_URL = process.env.VUE_APP_API_BASE_URL;


// Create an Axios instance
const apiClient = axios.create({
  baseURL: VUE_APP_API_BASE_URL,
  timeout: 10000,
});

// Add a request interceptor
apiClient.interceptors.request.use(
  (config) => {
    const token = store.state.accessToken;
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
    // Error handling logic
    if (error.response.status === 401 && !error.config._retry) {
      // If 401 is received, try refreshing the token and retrying the request once
      error.config._retry = true;
      await store.dispatch('refreshTokens');
      error.config.headers.Authorization = `Bearer ${store.state.accessToken}`;
      return apiClient(error.config);
    }
    return Promise.reject(error);
  }
);

export default apiClient;
