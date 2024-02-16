// stores/auth.js
import { defineStore } from 'pinia';
import apiClient from '../axios';

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: null,
        token: localStorage.getItem('token') || null,
    }),
    getters: {
        isAuthenticated: (state) => !!state.token,
    },
    actions: {
        async confirmAccount(token) {
            return new Promise((resolve, reject) => {
                apiClient
                    .get(`${process.env.VUE_APP_API_BASE_URL}/api/users/confirm/${token}`)
                    .then(() => {
                        resolve("Your account has been successfully confirmed. You can now login.");
                    })
                    .catch(error => {
                        console.error("Error confirming account:", error.response.data);
                        reject("There was an error confirming your account. Please try again or contact support.");
                    });
            });
        },
        async login(credentials) {
            try {
                const response = await apiClient.post('/api/users/login/', credentials);
                this.user = response.data.user;
                this.token = response.data.access_token;
                localStorage.setItem('accessToken', this.token);
                localStorage.setItem('refreshToken', response.data.refresh_token);
                localStorage.setItem('user', JSON.stringify(response.data.user));
                apiClient.defaults.headers.common['Authorization'] = `Bearer ${this.token}`;
            } catch (error) {
                console.error('Login error', error);
                throw error;
            }
        },
        logout() {
            this.user = null;
            this.token = null;
            localStorage.removeItem('user');
            localStorage.removeItem('token');
            delete apiClient.defaults.headers.common['Authorization'];
        },
        async register(credentials) {
            try {
                await apiClient.post('/api/users/register/', credentials);
                this.login(credentials);
            } catch (error) {
                console.error('Registration error:', error);
                throw error;
            }
        },
        async refreshToken() {
            try {
                const refreshToken = localStorage.getItem('refreshToken'); // Assuming you store refreshToken
                if (!refreshToken) {
                    throw new Error("No refresh token available");
                }

                const response = await apiClient.post('/token/refresh/', {
                    refresh: refreshToken,
                });

                this.token = response.data.access; // Assuming the API returns a new access token named 'access'
                localStorage.setItem('token', this.token);
                apiClient.defaults.headers.common['Authorization'] = `Bearer ${this.token}`;
            } catch (error) {
                console.error('Token refresh error:', error);
                // Handle token refresh failure, e.g., by logging out the user
                this.logout();
            }
        },
        async fetchUser() {
            if (!this.token) {
                // Handle case where there is no token
                return;
            }
            try {
                const response = await apiClient.get('/api/users/', {
                    headers: { Authorization: `Bearer ${this.token}` },
                });
                this.user = response.data;
            } catch (error) {
                console.error('Error fetching user:', error);
                // Handle error, e.g., by clearing the token and redirecting to login
            }
        },
    },
});
