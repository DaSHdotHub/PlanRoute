import { createApp } from 'vue'
import App from './App.vue'
import BootstrapVue3 from 'bootstrap-vue-3'
import router from './router'
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'

axios.interceptors.response.use(response => response, async error => {
    const originalRequest = error.config;
  
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      const refreshToken = localStorage.getItem('refresh_token');
      if (refreshToken) {
        try {
          const response = await axios.post('http://127.0.0.1:8000/api/token/refresh/', { refresh: refreshToken });
          const newAccessToken = response.data.access;
          localStorage.setItem('access_token', newAccessToken);
          axios.defaults.headers.common['Authorization'] = `Bearer ${newAccessToken}`;
          return axios(originalRequest);
        } catch (refreshError) {
          console.error('Token refresh error:', refreshError);
          // Redirect to login or handle token refresh failure
          router.push({ name: 'Login' });
        }
      }
    }
  
    return Promise.reject(error);
  });

  const app = createApp(App);

  // Register BootstrapVue3
  app.use(BootstrapVue3);
  
  // Register router
  app.use(router);
  
  // Mount the application
  app.mount('#app');
  