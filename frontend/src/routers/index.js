import HomePage from '../components/HomePage.vue'
import SignUp from '../components/SignUp.vue'
import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '../components/LoginPage.vue'
import FaqPage from '../components/FaqPage.vue'
import Indices from '../views/Indices.vue'
import Sectors from '../views/Sectors.vue'
import Shares from '../views/Shares.vue'

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
    path: '/indices',
    name: 'Indices',
    component: Indices
},
{
    path: '/sectors',
    name: 'Sectors',
    component: Sectors
},
{
    path: '/shares',
    name: 'Shares',
    component: Shares
},
{
  path: "/FaqPage",
  name: "FaqPage",
  component: FaqPage,
},

];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;