import mainPage from "./views/mainPage.vue";
import categoryPage from "./views/categoryPage.vue";
import youtuberPage from "./views/youtuberPage.vue";
import searchPage from "./views/searchPage.vue";


export default [{
        path: "/",
        name: "mainPage",
        component: mainPage
    },
    {
        path: "/categoryPage",
        name: "categoryPage",
        component: categoryPage
    },
    {
        path: "/youtuberPage",
        name: "youtuberPage",
        component: youtuberPage
    },
    {
        path: "/searchPage",
        name: "searchPage",
        component: searchPage
    },


];