<template>
    <div class="email-confirmation">
        <h1>Email Confirmation</h1>
        <div v-if="loading">
            Checking your confirmation token...
        </div>
        <div v-else>
            <div v-if="confirmed">
                <p>Your email has been successfully confirmed!</p>
                <!-- Link to login -->
                <router-link to="/login">Go to Login</router-link>
            </div>
            <div v-else>
                <p>Invalid or expired token. Please try registering again or contact support.</p>
                <!-- Link to registration -->
                <router-link to="/register">Register</router-link>
            </div>
        </div>
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
    data() {
        return {
            loading: true,
            confirmed: false
        };
    },
    created() {
        this.confirmEmail();
    },
    methods: {
        confirmEmail() {
            // Extract the token from the URL
            const token = this.$route.params.token;

            axios.get(`http://127.0.0.1:8000/api/users/confirm/${token}`)
                .then(() => {
                    this.confirmed = true;
                })
                .catch(error => {
                    console.error('Confirmation error:', error);
                    this.confirmed = false;
                })
                .finally(() => {
                    this.loading = false;
                });
        }
    }
};
</script>
  
<style>
.email-confirmation {
    text-align: center;
    padding: 20px;
}
</style>
  