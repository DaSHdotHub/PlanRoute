import { createApp } from 'vue'
import App from './App.vue'
import BootstrapVue3 from 'bootstrap-vue-3'
import router from './router'
import axios from 'axios';
import './assets/global.css';
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'

// Function to get CSRF token
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Set Axios default configuration
axios.defaults.withCredentials = true;
axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
axios.defaults.headers.common['X-CSRFToken'] = getCookie('csrftoken');

// Axios interceptor for handling token refresh
axios.interceptors.response.use(response => response, async error => {
    const originalRequest = error.config;
  
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      const refreshToken = localStorage.getItem('refresh_token');
      axios.defaults.baseURL = process.env.VUE_APP_API_BASE_URL;
      if (refreshToken) {
        try {
          const response = await axios.post('/api/token/refresh/', { refresh: refreshToken });
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
  