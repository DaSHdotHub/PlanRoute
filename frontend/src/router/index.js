import { createRouter, createWebHistory } from "vue-router";
import AboutPage from "@/views/AboutPage.vue";
import LandingPage from "@/views/LandingPage.vue";
import UserDashboard from "@/views/UserDashboard.vue";
import UserLogin from "@/components/UserLogin.vue";
import UserRegister from "@/components/UserRegister.vue";
import ViewPatient from "@/components/ViewPatient.vue";
import EditPatient from "@/components/EditPatient.vue";
import TokenRedirect from "@/components/TokenRedirect.vue";

const routes = [
  { path: "/", name: "Home", component: LandingPage },
  { path: "/login", name: "Login", component: UserLogin },
  { path: "/register", name: "Register", component: UserRegister },
  { path: "/dashboard", name: "Dashboard", component: UserDashboard },
  { path: "/about", name: "About", component: AboutPage },
  { path: "/patients/:id/view", name: "ViewPatient", component: ViewPatient },
  { path: "/patients/:id/edit", name: "EditPatient", component: EditPatient },
  { path: "/redirect/:token", name: "TokenRedirect", component: TokenRedirect },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
