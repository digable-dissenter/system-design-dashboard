import HomePage from './components/HomePage.vue'
import SignUp from './components/SignUp.vue'
import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from './components/LoginPage.vue'
import StaticReports from './components/StaticReports.vue'

const routes = [{
    name: 'HomePage',
    component: HomePage,
    path: '/'
},
{
    name: 'SignUp',
    component: SignUp,
    path: '/sign-up'
},
{
    name: 'LoginPage',
    component: LoginPage,
    path: '/login'
},

 {
    path: "/static-reports",
    name: "StaticReports",
    component: StaticReports,
  },

];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;