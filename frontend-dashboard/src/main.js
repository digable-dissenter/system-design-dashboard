import { createApp } from 'vue';
import App from './App.vue';
import router from './routers';
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap.css'
Vue.use(BootstrapVue)
createApp(App)
.use(router)
.mount('#app');
