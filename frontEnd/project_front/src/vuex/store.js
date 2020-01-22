import Vue from "vue";
import Vuex from "vuex";
import actions from "./actions";
import mutations from "./mutations";

Vue.use(Vuex);

const state = {
    testID: "",
    items: [{
            text: 'Home',
            to: '/'
        },
        {
            text: 'Top5',
            to: '/categoryPage'
        }
    ]
};

const getters = {

    links: state => {
        return state.items
    }

}

export default new Vuex.Store({
    state,
    getters,
    mutations,
    actions
});


Vue.use(Vuex)