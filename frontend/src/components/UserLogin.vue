<template>
  <div class="login-container">
    <form @submit.prevent="login">
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" id="username" v-model="username">
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password">
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    async login() {
      try {
        axios.defaults.baseURL = process.env.VUE_APP_API_BASE_URL;
        const response = await axios.post('/api/token/', {
          username: this.username,
          password: this.password
        });
        localStorage.setItem('access_token', response.data.access);
        localStorage.setItem('refresh_token', response.data.refresh);
        axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;
        this.$router.push({ name: 'Dashboard' });
      } catch (error) {
        console.error('Login error:', error);
        // TODO: handle login error
      }
    }
  }
};
</script>