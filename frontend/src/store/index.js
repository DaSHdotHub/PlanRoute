import axios from 'axios';
const VUE_APP_API_BASE_URL = process.env.VUE_APP_API_BASE_URL;
import { createStore } from 'vuex';

export default createStore({
    state: {
        accessToken: null,
        refreshToken: null,
        user: null,
    },
    mutations: {
        setTokens(state, { accessToken, refreshToken }) {
            state.accessToken = accessToken;
            state.refreshToken = refreshToken;
        },
        setUser(state, user) {
            state.user = user;
        },
        logout(state) {
            state.accessToken = null;
            state.refreshToken = null;
            state.user = null;
        },
    },
    actions: {
        async login({ commit }, credentials) {
            try {
                const loginURL = `${VUE_APP_API_BASE_URL}/api/users/login/`;
                const response = await axios.post(loginURL, credentials);
                commit('setTokens', { accessToken: response.data.accessToken, refreshToken: response.data.refreshToken });
                return response;
            } catch (error) {
                console.error('Login error:', error);
                // Handle error (e.g., show notification)
            }
        },
        async register({ commit }, credentials) {
            try {
                const registerURL = `${VUE_APP_API_BASE_URL}/api/users/register/`;
                const response = await axios.post(registerURL, credentials);
                commit('setTokens', { accessToken: response.data.accessToken, refreshToken: response.data.refreshToken });
            } catch (error) {
                console.error('Registration error:', error);
                // Handle error
            }
        },
        async refreshTokens({ commit, state }) {
            try {
                const refreshURL = `${VUE_APP_API_BASE_URL}/api/token/refresh/`;
                const response = await axios.post(refreshURL, { refreshToken: state.refreshToken });
                commit('setTokens', { accessToken: response.data.accessToken, refreshToken: response.data.refreshToken });
            } catch (error) {
                console.error('Token refresh error:', error);
                // Handle error
            }
        },
        async fetchUser({ commit, state }) {
            try {
                const userURL = `${VUE_APP_API_BASE_URL}/api/users/`;
                const response = await axios.get(userURL, { headers: { Authorization: `Bearer ${state.accessToken}` } });
                commit('setUser', response.data);
            } catch (error) {
                console.error('Fetch user error:', error);
                // Handle error
            }
        }
    }
});
