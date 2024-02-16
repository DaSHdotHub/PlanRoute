<template>
  <div class="register-container container mt-5">
    <h1 class="mb-4">Register</h1>
    <form @submit.prevent="register" class="border p-4 rounded">
      <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="user.username" class="form-control" />
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="user.email" class="form-control" />
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="user.password" class="form-control" @input="checkPasswordStrength" />
        <div :class="`strength-meter mt-2 strength-${passwordStrength}`"></div>
      </div>
      <div class="form-group">
        <label for="confirmPassword">Confirm Password:</label>
        <input type="password" id="confirmPassword" v-model="confirmPassword" class="form-control" />
        <div v-if="passwordMismatch" class="alert alert-warning mt-2">Passwords do not match.</div>
      </div>
      <div class="form-group form-check">
        <input type="checkbox" id="is_editor" class="form-check-input" v-model="user.is_editor" />
        <label for="is_editor" class="form-check-label">Register as editor</label>
      </div>
      <button type="submit" class="btn btn-primary" :disabled="passwordMismatch">Register</button>
    </form>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useAuthStore } from '../stores/auth'; // Update the path as necessary
import { useRouter } from 'vue-router';

const user = ref({
  username: '',
  email: '',
  password: '',
  is_editor: false,
});
const confirmPassword = ref('');
const authStore = useAuthStore();
const router = useRouter();
const errorMessage = ref('');

const passwordStrength = ref('');
const passwordMismatch = computed(() => user.value.password !== confirmPassword.value);

const checkPasswordStrength = () => {
  const password = user.value.password;
  if (password.length < 6) {
    passwordStrength.value = 'weak';
  } else if (password.length >= 6 && password.length < 10) {
    passwordStrength.value = 'medium';
  } else {
    passwordStrength.value = 'strong';
  }
};

const register = async () => {
  if (passwordMismatch.value) {
    errorMessage.value = 'Passwords do not match.';
    return;
  }

  try {
    await authStore.register({
      username: user.value.username,
      email: user.value.email,
      password: user.value.password,
      is_editor: user.value.is_editor,
    });
    router.push({ name: 'Home' });
  } catch (error) {
    errorMessage.value = error.message || 'An error occurred during registration.';
  }
};
</script>

<style scoped>
.register-container {
  font-family: 'Roboto', sans-serif;
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
