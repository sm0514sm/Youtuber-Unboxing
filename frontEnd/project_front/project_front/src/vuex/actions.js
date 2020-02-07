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
        console.log("action_GET_YOUTUBER ");

        var yno = payload.yno
        var callback = payload.callback
        var failCallback = payload.failCallback

        //youtuber 기본정보
        const BasicImpormation = new Promise((resolve, reject) => {
            http
                .get("/youtuber/" + yno)
                .then(response => {
                    resolve(response.data.data);
                })
                .catch(err => {
                    reject(err);
                });
        });


        // activity : youtuber 활동력 최근 {{month}}간 몇개의 영상을 올렸는지
        var month = 1
        const videoDuringMonth = new Promise((resolve, reject) => {
            http
                .get("/youtuber/detail/activity/videoCount/" + yno + "_" + month)
                .then(response => {
                    resolve(response.data.data);
                })
                .catch(err => {
                    reject(err);
                });
        });

        // activity : youtuber {{week}}주동안 영상 업로드 수
        var week = 4
        const video4Weeks = new Promise((resolve, reject) => {
            http
                .get("/youtuber/detail/activity/termVideoCount/" + yno + "_" + week)
                .then(response => {
                    resolve(response.data.data);
                })
                .catch(err => {
                    reject(err);
                });
        });

        // charm : 최근 {{recent}}개의 전체 좋아요비율
        var recent = 10
        const entiregoodratio = new Promise((resolve, reject) => {
            http
                .get("/youtuber/detail/charm/goodRatio/" + yno + "_" + recent)
                .then(response => {
                    resolve(response.data.data);
                })
                .catch(err => {
                    reject(err);
                });
        });

        // charm : 최근 {{videoCount}}개의 각 동영상의 좋아요 비율
        var videoCount = 3
        const goodRatioperVideo = new Promise((resolve, reject) => {
            http
                .get("/youtuber/detail/charm/video/" + yno + "_" + videoCount)
                .then(response => {
                    resolve(response.data.data);
                })
                .catch(err => {
                    reject(err);
                });
        });




        Promise.all([BasicImpormation, videoDuringMonth, video4Weeks, entiregoodratio, goodRatioperVideo]).then(
            axios.spread((...responses) => {


                for (var i = 0; i < responses.length; i++) {
                    console.log(responses[i])
                }
                callback(...responses)

            })
        ).catch(
            failCallback()

        );
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
    },

    [Constant.GET_MANYTOP5]: (store) => {
        // var callback = payload.callback;

        const subscriber = new Promise((resolve, reject) => {
            http
                .get("/youtuber/rank/subscriber_5")
                .then(response => {
                    resolve(response.data.data);
                })
                .catch(err => {
                    reject(err);
                });
        });

        const totalViewCount = new Promise((resolve, reject) => {
            http
                .get("/youtuber/rank/totalViewCount_5")
                .then(response => {
                    resolve(response.data.data);
                })
                .catch(err => {
                    reject(err);
                });
        });

        const totalVideoCount = new Promise((resolve, reject) => {
            http
                .get("/youtuber/rank/totalVideoCount_5")
                .then(response => {
                    resolve(response.data.data);
                })
                .catch(err => {
                    reject(err);
                });
        });

        const grade = new Promise((resolve, reject) => {
            http
                .get("/youtuber/rank/grade_5")
                .then(response => {
                    resolve(response.data.data);
                })
                .catch(err => {
                    reject(err);
                });
        });

        const clickCount = new Promise((resolve, reject) => {
            http
                .get("/youtuber/rank/clickCount_5")
                .then(response => {
                    resolve(response.data.data);
                })
                .catch(err => {
                    reject(err);
                });
        });



        Promise.all([subscriber, totalViewCount, totalVideoCount, grade, clickCount]).then(
            axios.spread((...responses) => {

                var list = []
                var titles = ["구독자", "총영상조회수", "총영상수", "등급", "사이트조회수"]

                for (var i = 0; i < responses.length; i++) {
                    list.push({ title: titles[i], list: responses[i] })
                }

                console.log(list)

                // callback(responses[0], responses[1]);

                store.commit(Constant.GET_MANYTOP5, {
                    list: list
                });

            })
        );



    }

};