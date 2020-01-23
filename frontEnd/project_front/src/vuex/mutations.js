import Constant from "./Constant";
import store from "./store";

export default {
    [Constant.GET_TEST]: (state, payload) => {
        store.state.testID = payload.testID;
    },
    [Constant.GET_YOUTUBERS_PER_CATEGORY]: (state, payload) => {
        store.state.youtubersPerCategory = payload.youtuberslist;
    },
    [Constant.CHANGE_CATEGORY_LOADING]: (state, payload) => {
        store.state.isCategoryLoading = payload.bool;
    }
};