import Vue from 'vue';
import VueRouter from 'vue_router';
import Frontview from '..components/Frontview.vue';
import SignUp from '..components/SignUp.vue';

Vue.use(VueRouter);

export default new VueRouter({
    mode:'history',
    routes:[
        {
            path:'/',
            name:'Frontview',
            component: Frontview,
        },
        {
            path:'/signup',
            name:'SignUp',
            component: SignUp,
        },
    ],
})