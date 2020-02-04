import Vue from "vue";
import App from "./App.vue";
import Router from "vue-router";
import routes from "./routes";
import store from "./vuex/store";
import vuetify from './plugins/vuetify';
import imagePreloader from 'vue-image-preloader'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueApexCharts from 'vue-apexcharts'
Vue.use(VueApexCharts)




Vue.config.productionTip = false;
Vue.config.devtools = true;

Vue.use(Router);
Vue.use(imagePreloader)
Vue.use(BootstrapVue)
Vue.component('apexchart', VueApexCharts)


const router = new Router({
    mode: 'history',
    routes
});

new Vue({
    router,
    store,
    vuetify,
    render: h => h(App)
}).$mount("#app");