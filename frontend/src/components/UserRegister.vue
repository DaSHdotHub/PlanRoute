<template>
  <div class="register-container container mt-5">
    <h1 class="mb-4" style="font-weight: 500">Register</h1>
    <form @submit.prevent="register" class="border p-4 rounded">
      <!-- Display error message -->
      <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
      <div class="form-group">
        <label for="username">Username:</label>
        <input
          type="text"
          id="username"
          v-model="user.username"
          class="form-control"
        />
      </div>

      <div class="form-group">
        <label for="email">Email:</label>
        <input
          type="email"
          id="email"
          v-model="user.email"
          class="form-control"
        />
      </div>

      <div class="form-group">
        <label for="password">Password:</label>
        <input
          type="password"
          id="password"
          v-model="user.password"
          class="form-control"
          @input="checkPasswordStrength"
        />
        <!-- Password strength indicator -->
        <div :class="`strength-meter mt-2 strength-${passwordStrength}`"></div>
      </div>

      <div class="form-group">
        <label for="confirmPassword">Confirm Password:</label>
        <input
          type="password"
          id="confirmPassword"
          v-model="confirmPassword"
          class="form-control"
        />
        <!-- Password match message -->
        <div v-if="passwordMismatch" class="alert alert-warning mt-2">
          Passwords do not match.
        </div>
      </div>

      <div class="form-group form-check">
        <input
          type="checkbox"
          id="is_editor"
          class="form-check-input"
          v-model="user.is_editor"
        />
        <label for="is_editor" class="form-check-label"
          >Register as editor</label
        >
      </div>

      <button
        type="submit"
        class="btn btn-primary"
        :disabled="passwordMismatch"
      >
        Register
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";

const user = ref({
  username: "",
  email: "",
  password: "",
  is_editor: false,
});
const confirmPassword = ref("");
const store = useStore();
const router = useRouter();
const errorMessage = ref("");

const passwordStrength = ref("");
const passwordMismatch = computed(
  () => user.value.password !== confirmPassword.value
);

const checkPasswordStrength = () => {
  const password = user.value.password;
  if (password.length < 6) {
    passwordStrength.value = "weak";
  } else if (password.length >= 6 && password.length < 10) {
    passwordStrength.value = "medium";
  } else {
    passwordStrength.value = "strong";
  }
};

const register = async () => {
  try {
    await store.dispatch("register", user.value);
    router.push({ name: "Home" });
  } catch (error) {
    if (error.response && error.response.status === 400) {
      errorMessage.value =
        "Username or email already in use. Please try again.";
    } else if (error.request) {
      // Request was made but no response was received
      errorMessage.value =
        "The request was made but no response was received. Please check your network and try again.";
      console.error("Error request:", error.request);
    } else {
      // Something happened in setting up the request that triggered an Error
      errorMessage.value =
        "An error occurred while trying to register. Please try again later.";
      console.error("Error message:", error.message);
    }
  }
};
</script>
<style scoped>
.register-container {
  font-family: "Roboto", sans-serif;
}

.strength-meter {
  height: 5px;
  border-radius: 5px;
}

.strength-weak {
  background-color: #ff6a6a;
}

.strength-medium {
  background-color: #ffdd5e;
}

.strength-strong {
  background-color: #28a745;
}

.alert {
  font-size: 0.9rem;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 20px;
}
</style>
