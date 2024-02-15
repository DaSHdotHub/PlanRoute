import { createApp } from 'vue';
import App from './App.vue';
import BootstrapVue3 from 'bootstrap-vue-3';
import router from './router';
import store from './store';
import axios from 'axios';
import './assets/global.css';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css';

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
axios.defaults.baseURL = process.env.VUE_APP_API_BASE_URL;

// Axios interceptor for handling token refresh
axios.interceptors.response.use(response => response, async error => {
  if (error.response.status === 401 && !error.config._retry) {
    error.config._retry = true;
    try {
      // Attempt to refresh tokens using Vuex action
      await store.dispatch('refreshTokens');
      // Update the Authorization header with the new access token
      error.config.headers['Authorization'] = `Bearer ${store.state.accessToken}`;
      // Retry the original request with the new token
      return axios(error.config);
    } catch (refreshError) {
      console.error('Token refresh error:', refreshError);
      // Logout the user or redirect to login if token refresh fails
      await store.dispatch('logout');
      router.push({ name: 'Login' });
      return Promise.reject(refreshError);
    }
  }
  return Promise.reject(error);
});

const app = createApp(App);

// Register Vuex store
app.use(store);

// Register BootstrapVue3
app.use(BootstrapVue3);

// Register router
app.use(router);

// Mount the application
app.mount('#app');
