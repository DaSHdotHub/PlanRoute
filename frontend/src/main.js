import { createApp } from 'vue';
import { createPinia } from 'pinia';
import  BootstrapVue3  from 'bootstrap-vue-3';
import App from './App.vue';
import router from './router';
import './assets/global.css';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css';

const app = createApp(App);
const pinia = createPinia();

// Register pinia store
app.use(pinia);

// Register BootstrapVue3
app.use(BootstrapVue3);

// Register router
app.use(router);

// Mount the application
app.mount('#app');