import Vue from "vue";
import App from "./App.vue";
import Router from "vue-router";
import routes from "./routes";
import store from "./vuex/store";
import vuetify from './plugins/vuetify';
import imagePreloader from 'vue-image-preloader'


Vue.config.productionTip = false;
Vue.config.devtools = true;

Vue.use(Router);
Vue.use(imagePreloader)

const router = new Router({
    routes
});

new Vue({
    router,
    store,
    vuetify,
    render: h => h(App)
}).$mount("#app");