<template>
    <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="#">Your Logo Here</b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav class="ml-auto">
                <b-button @click="goToLandingPage">Home</b-button>
                <b-button @click="goToAboutPage">About</b-button>
                <b-button @click="goToLogin" variant="primary" class="mr-2">Login</b-button>
                <b-button @click="goToRegister" variant="success">Register</b-button>
            </b-navbar-nav>
        </b-collapse>
    </b-navbar>
</template>

<script>
export default {
    methods: {
        goToLogin() {
            this.$router.push({ name: 'Login' });
        },
        goToRegister() {
            this.$router.push({ name: 'Register' });
        },
        goToAboutPage() {
            this.$router.push({ name: 'About' });
        },
        goToLandingPage() {
            this.$router.push({ name: 'Home' });
        }
    }
};
</script>

<style scoped>
/* Styling for the header */
header {
    background-color: #98ff98; /* Mint color */
    color: white;
    padding: 1rem 0;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.navbar-brand {
    font-size: 1.5rem;
    font-weight: bold;
}
</style>