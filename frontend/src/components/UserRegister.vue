<template>
  <div class="register-container container mt-5">
    <h1 class="mb-4" style="font-weight: 500;">Register</h1>
    <form @submit.prevent="register" class="border p-4 rounded">
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="user.username" class="form-control">
      </div>

      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="user.email" class="form-control">
      </div>

      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="user.password" class="form-control">
      </div>

      <div class="form-group form-check">
        <input type="checkbox" id="is_editor" class="form-check-input" v-model="user.is_editor">
        <label for="is_editor" class="form-check-label">Register as editor</label>
      </div>

      <button type="submit" class="btn btn-primary">Register</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      user: {
        username: '',
        email: '',
        password: '',
        is_editor: false
      }
    };
  },
  methods: {
    async register() {
      try {
        axios.defaults.baseURL = process.env.VUE_APP_API_BASE_URL;
        const response = await axios.post('/api/users/register/', this.user);
        console.log('Registration successful', response);
        // Redirect or further actions after successful registration
      } catch (error) {
        console.error('Registration error', error);
      }
    }
  }
};
</script>

<style scoped>
.register-container {
  font-family: 'Roboto', sans-serif;
}

/* Use heavier weight for heading */

h1 {
  font-weight: 700;
}
</style>