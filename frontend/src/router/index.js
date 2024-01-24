import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '@/components/LandingPage.vue';
import Login from '@/components/UserLogin.vue';
import Register from '@/components/UserRegister.vue';
import Dashboard from '@/components/UserDashboard.vue';

const routes = [
  { path: '/', name: 'Home', component: LandingPage },
  { path: '/login', name: 'Login', component: Login },
  { path: '/register', name: 'Register', component: Register },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard }

  // ... other routes ...
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
