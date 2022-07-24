import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../components/HomePage.vue";
import SignUp from "../components/SignUp.vue";
import LoginPage from "../components/LoginPage.vue";
import StaticReports from "../components/StaticReports.vue";

const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
  },
  {
    path: "/sign-up",
    name: "SignUp",
    component: SignUp,
  },
  {
    path: "/login",
    name: "LoginPage",
    component: LoginPage,
  },
  {
    path: "/static-reports",
    name: "StaticReports",
    component: StaticReports,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
