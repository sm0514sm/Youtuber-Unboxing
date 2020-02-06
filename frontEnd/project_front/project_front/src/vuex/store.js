import Vue from "vue";
import Vuex from "vuex";
import actions from "./actions";
import mutations from "./mutations";

Vue.use(Vuex);

const state = {
    items: [{
            text: 'Home',
            to: '/',
            name: "mainPage"
        },
        {
            text: 'Top5',
            to: '/categoryPage',
            name: "categoryPage"
        }
    ],
    category: [{
            nameEng: "game",
            nameKor: "게임",
            cano: 1,
        },
        {
            nameEng: "entertainment",
            nameKor: "엔터",
            cano: 2,
        },
        {
            nameEng: "beauty",
            nameKor: "뷰티",
            cano: 3,
        },
        {
            nameEng: "sports",
            nameKor: "운동",
            cano: 4,

        },
        {
            nameEng: "mukbang",
            nameKor: "먹방",
            cano: 5,
        },
        {
            nameEng: "kids",
            nameKor: "키즈",
            cano: 6,

        },
        {
            nameEng: "animals",
            nameKor: "동물",
            cano: 7,

        },
        {
            nameEng: "life",
            nameKor: "일상",
            cano: 8,
        },
        {
            nameEng: "it",
            nameKor: "IT",
            cano: 9,

        },
    ],
    youtubersPerCategory: [],
    isCategoryLoading: false,
    currentCategory: "life",
    youtuber: {},
    searchyoutuber: [],
    compareyoutuber: ["aaaaaa", "Bbbbbbbba"]
};

const getters = {
    categories: state => {

        return state.category
    },
    links: state => {
        return state.items
    },
    youtubersPerCategory: state => {
        return state.youtubersPerCategory
    },
    youtuber: state => {
        return state.youtuber
    },
    searchyoutuber: state => {
        return state.searchyoutuber
    },
    compareyoutuber: state => {
        return state.compareyoutuber
    }
}

export default new Vuex.Store({
    state,
    getters,
    mutations,
    actions
});


Vue.use(Vuex)