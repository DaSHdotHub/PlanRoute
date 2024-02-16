<template>
  <b-navbar toggleable="lg" type="dark" variant="primary" class="navbar-custom">
    <b-navbar-brand href="#" class="navbar-logo">PlanRoute</b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav class="ml-auto">
        <b-button
          @click="goToLandingPage"
          variant="outline-light"
          class="mx-3 custom-button"
          >Home</b-button
        >
        <b-button
          @click="goToAboutPage"
          variant="outline-light"
          class="mx-3 custom-button"
          >About</b-button
        >
        <template v-if="!user">
          <b-button
            @click="goToLogin"
            variant="outline-primary"
            class="mx-3 custom-button"
            >Login</b-button
          >
          <b-button
            @click="goToRegister"
            variant="outline-success"
            class="mx-3 custom-button"
            >Register</b-button
          >
        </template>
        <template v-else>
          <b-button
            @click="logout"
            variant="outline-danger"
            class="mx-3 custom-button"
            >Logout</b-button
          >
        </template>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
import { useAuthStore } from "../../stores/auth";
import { useRouter } from "vue-router";

export default {
  setup() {
    const authStore = useAuthStore();
    const router = useRouter();
    const user = JSON.parse(localStorage.getItem("user"));

    const goToLogin = () => {
      router.push({ name: "Login" });
    };
    const goToRegister = () => {
      router.push({ name: "Register" });
    };
    const goToAboutPage = () => {
      router.push({ name: "About" });
    };
    const goToLandingPage = () => {
      router.push({ name: "Home" });
    };

    const logout = async () => {
      await authStore.logout();
      router.push({ name: "Home" });
    };

    return {
      user,
      goToLogin,
      goToRegister,
      goToAboutPage,
      goToLandingPage,
      logout,
    };
  },
};
</script>

<style scoped>
/* Custom styling for the navbar */
.navbar-custom {
  background-color: #1e90ff;
}

.navbar-logo {
  font-size: 2rem; 
  font-weight: bold; 
  font-family: 'Arial', sans-serif;
  color: #fff;
}

.custom-button {
  color: #fff; 
  border-color: #fff;
}

.custom-button:hover {
  background-color: #fff; 
  color: #000; 
  border-color: #000; 
}

/* Apply shadow for elevation */
.b-navbar-nav .b-nav-item .b-nav-link {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

/* Lift the button slightly on hover */
.b-navbar-nav .b-nav-item .b-nav-link:hover {
  transform: translateY(-1px);
}
</style>
