import Constant from "./Constant";
import http from "./http-common";
import axios from "axios"

export default {
    [Constant.GET_TEST]: store => {
        http
            .get("/test/")
            .then(response => {
                console.log(response.data.data);
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
        console.log("action_GET_YOUTUBERS_PER_CATEGORY " + payload.category);
        http
            .get("/category/" + payload.category)
            .then(response => {
                console.log(response.data.data[0]);
                store.commit(Constant.GET_YOUTUBERS_PER_CATEGORY, {
                    youtuberslist: response.data.data
                });
            })
            .catch(exp => {
                alert("GET_YOUTUBERS_PER_CATEGORY에 실패하였습니다\n" + exp);
            });
    },
    [Constant.GET_YOUTUBER]: (store, payload) => {
        console.log("action_GET_YOUTUBER " + store.state.youtuber);
        //store.commit(Constant.CHANGE_CATEGORY_LOADING, { bool: true });
        http
            .get("/youtuber/" + payload.yno)
            .then(response => {
                console.log(response.data.data);
                store.commit(Constant.GET_YOUTUBER, {
                    youtuber: response.data.data
                });
                //store.commit(Constant.CHANGE_CATEGORY_LOADING, { bool: false });
            })
            .catch(exp => {
                alert("GET_YOUTUBER 실패하였습니다\n" + exp);
            });
    },
    [Constant.SEARCH_YOUTUBER]: (store, payload) => {
        console.log("action-SEARCH_YOUTUBER " + payload.searchWord);
        //store.commit(Constant.CHANGE_CATEGORY_LOADING, { bool: true });
        http
            .get("/youtuber/search/" + payload.searchWord)
            .then(response => {
                console.log(response.data.data);
                store.commit(Constant.SEARCH_YOUTUBER, {
                    youtubers: response.data.data
                });
                //store.commit(Constant.CHANGE_CATEGORY_LOADING, { bool: false });
            })
            .catch(exp => {
                alert("GET_YOUTUBER 실패하였습니다\n" + exp);
            });
    },
    [Constant.GET_COMPARE_YOUTUBER]: (store, payload) => {

        var youtuber1 = payload.youtuber1;
        var youtuber2 = payload.youtuber2;
        var callback = payload.callback;

        const youtuber1Search = new Promise((resolve, reject) => {
            http
                .get("/youtuber/" + youtuber1.yno)
                .then(response => {
                    resolve(response.data.data);
                })
                .catch(err => {
                    reject(err);
                });
        });

        const youtuber2Search = new Promise((resolve, reject) => {
            http
                .get("/youtuber/" + youtuber2.yno)
                .then(response => {
                    resolve(response.data.data);
                })
                .catch(err => {
                    reject(err);
                });
        });

        Promise.all([youtuber1Search, youtuber2Search]).then(
            axios.spread((...responses) => {

                console.log(responses[0], responses[1])

                callback(responses[0], responses[1]);


            })
        );
    },

    [Constant.INSERT_YOUTUBUER]: (store, payload) => {
        //통신하기
        console.log("INSERT_YOUTUBUER" + payload.address)

        //통신하고 완료되면 then 
        //code
        var code = Math.floor(Math.random() * (2 + 11) - 11);

        //yno
        var yno = 45
        code = 0

        var callback = payload.callback
        setTimeout(function() {
            callback(code, yno)
        }, 2000)



    }

};