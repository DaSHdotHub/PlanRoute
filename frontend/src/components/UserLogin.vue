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
        const response = await axios.post('http://127.0.0.1:8000/api/token/', {
          username: this.username,
          password: this.password
        });
        this.$emit('auth-success', response.data);
        localStorage.setItem('access_token', response.data.access);
        axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;
      } catch (error) {
        console.error('Login error:', error);
      }
    }
  }
};
</script>
