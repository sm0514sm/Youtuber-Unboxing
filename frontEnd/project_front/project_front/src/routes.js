import mainPage from "./views/mainPage.vue";
import categoryPage from "./views/categoryPage.vue";
import youtuberPage from "./views/youtuberPage.vue";
import searchPage from "./views/searchPage.vue";
import memberPage from "./views/memberPage.vue";


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
    {
        path: "/memberPage",
        name: "memberPage",
        component: memberPage
    },


];