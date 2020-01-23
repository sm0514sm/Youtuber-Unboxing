import Constant from "./Constant";
import http from "./http-common";

export default {
    [Constant.GET_TEST]: store => {
        http
            .get("/test/")
            .then(response => {
                console.log(response.data.data[0]);
                alert(response.data.data[0]);
                store.commit(Constant.GET_TEST, {
                    testID: response.data.data[0].id
                });
            })
            .catch(exp => {
                alert("TEST에 실패하였습니다\n" + exp);
            });
    },
    [Constant.GET_YOUTUBERS_PER_CATEGORY]: (store, payload) => {
        console.log("action_GET_YOUTUBERS_PER_CATEGORY" + payload.category);
        store.commit(Constant.CHANGE_CATEGORY_LOADING, { bool: true });
        http
            .get("/category/" + payload.category)
            .then(response => {
                console.log(response.data.data);
                store.commit(Constant.GET_YOUTUBERS_PER_CATEGORY, {
                    youtuberslist: response.data.data
                });
                store.commit(Constant.CHANGE_CATEGORY_LOADING, { bool: false });
            })
            .catch(exp => {
                alert("GET_YOUTUBERS_PER_CATEGORY에 실패하였습니다\n" + exp);
            });
    },
};