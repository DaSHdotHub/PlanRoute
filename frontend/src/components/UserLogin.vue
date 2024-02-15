<template>
  <div class="login-container">
    <form @submit.prevent="login">
      <!-- Display error message -->
      <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" id="username" v-model="username" />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" />
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";

const username = ref("");
const password = ref("");
const store = useStore();
const router = useRouter();
const errorMessage = ref("");

const login = async () => {
  try {
    const credentials = { username: username.value, password: password.value };
    const response = await store.dispatch("login", credentials);
    if (response.status === 200) {
      router.push({ name: "Dashboard" });
    } else {
      // Handle unexpected response status if necessary
      errorMessage.value = "An unexpected error occurred.";
    }
  } catch (error) {
    // Handle errors thrown from the Vuex action
    if (error.response && error.response.status === 401) {
      errorMessage.value = "Incorrect username or password. Please try again.";
    } else {
      errorMessage.value =
        "An error occurred while trying to log in. Please try again later.";
    }
  }
};
</script>

<style scoped>
.error-message {
  color: red;
  margin-bottom: 10px;
}
</style>
