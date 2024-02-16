<template>
  <div v-if="loading">Redirecting, please wait...</div>
  <div v-else>
    <p>{{ message }}</p>
    <button @click="redirectToLandingPage">Go to Main</button>
  </div>
</template>

<script>
import { useAuthStore } from "../stores/auth";

export default {
  name: "TokenRedirect",
  data() {
    return {
      loading: true,
      message: "",
    };
  },
  methods: {
    redirectToLandingPage() {
      this.$router.push({ name: "Home" });
    },
  },
  async mounted() {
    const authStore = useAuthStore();
    const token = this.$route.params.token;

    try {
      const message = await authStore.confirmAccount(token);
      this.message = message;
    } catch (error) {
      this.message = error;
    } finally {
      this.loading = false;
    }
  },
};
</script>

<style></style>
