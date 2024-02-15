<template>
  <div v-if="loading">Redirecting, please wait...</div>
  <div v-else>
    <p>{{ message }}</p>
    <button @click="redirectToLandingPage">Go to Main</button>
  </div>
</template>

<script>
import axios from "axios";

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
    confirmAccount() {
      const token = this.$route.params.token;
      const apiUrl = `${process.env.VUE_APP_API_BASE_URL}/api/users/confirm/${token}`;
      axios
        .get(apiUrl)
        .then(() => {
          this.message =
            "Your account has been successfully confirmed. You can now login.";
          this.loading = false;
        })
        .catch((error) => {
          console.error("Error confirming account:", error.response.data);
          this.message =
            "There was an error confirming your account. Please try again or contact support.";
          this.loading = false;
        });
    },
  },
  mounted() {
    this.confirmAccount();
  },
};
</script>

<style></style>
