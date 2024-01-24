<!-- LandingPage.vue -->
<template>
    <div class="container">
      <h1>Welcome to PlanRoute</h1>
      <button @click="goToLogin">Login</button>
      <button @click="goToRegister">Register</button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      goToLogin() {
        this.$router.push({ name: 'Login' });
      },
      goToRegister() {
        this.$router.push({ name: 'Register' });
      }
    }
  };
  </script>
  