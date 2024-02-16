<template>
  <div class="login-container container mt-5">
    <h1 class="mb-4" style="font-weight: 500">Login</h1>
    <form @submit.prevent="login" class="border p-4 rounded">
      <!-- Display error message -->
      <div v-if="errorMessage" class="alert alert-danger">{{ errorMessage }}</div>
      <div class="form-group">
        <label for="username">Username:</label>
        <input
          type="text"
          id="username"
          v-model="username"
          class="form-control"
        />
      </div>

      <div class="form-group">
        <label for="password">Password:</label>
        <input
          type="password"
          id="password"
          v-model="password"
          class="form-control"
        />
      </div>

      <button type="submit" class="btn btn-primary">
        Login
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '../stores/auth'; // Update the path as necessary
import { useRouter } from 'vue-router';

const username = ref('');
const password = ref('');
const authStore = useAuthStore();
const router = useRouter();
const errorMessage = ref('');

const login = async () => {
  try {
    await authStore.login({ username: username.value, password: password.value });
    router.push({ name: 'Dashboard' }); // Adjust the route as per your application
  } catch (error) {
    if (error.response && error.response.status === 401) {
      errorMessage.value = 'Incorrect username or password. Please try again.';
    } else {
      errorMessage.value = 'An error occurred while trying to log in. Please try again later.';
    }
  }
};
</script>

<style scoped>
.login-container {
  font-family: "Roboto", sans-serif;
}

.form-control {
  margin-bottom: 15px;
}

.alert {
  font-size: 0.9rem;
  margin-bottom: 20px;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 20px;
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
}
</style>
