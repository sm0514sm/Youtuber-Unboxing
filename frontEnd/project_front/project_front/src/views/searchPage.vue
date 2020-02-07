<template>
  <!-- vuetify를 참고하여 작성하기
  https://vuetifyjs.com/ko/components/api-explorer
  -->
  <v-container>
    <h1>searchPage</h1>
    "{{$route.query.word}}" 를 검색한 결과
    <!--youtuber-->
    <h1>Youtuber</h1>
    <hr />

    <v-container wrap style="background : gray">
      <v-card v-for="(item,i) in searchedyoutuber.slice(0,10)" :key="i" class="my-3" outlined flat @click="gotoYoutuberPage(item.yno)">
        <v-container fluid>
          <v-row>
            <!-- thumbnail -->
            <v-col cols="2" class="pa-3">
              <v-img class="circle" :src="item.thumbnails" flat :aspect-ratio="1/1" />
            </v-col>

            <!-- 기본정보 -->
            <v-col cols="8">
              <v-row>
                <v-col class="pb-0">
                  <p class="font-weight-black thin display-1 ma-0">{{item.channelName}}</p>
                </v-col>
              </v-row>
              <v-row>
                <v-col class="pa-0 pl-3">
                  <span class="font-weight-light">개설일 : {{item.publishedDate}} &nbsp;&nbsp;</span>
                </v-col>
              </v-row>
              <v-row>
                <v-col class="ma-0 pa-0">
                  <v-divider class="pa-0 ma-0"></v-divider>
                </v-col>
              </v-row>

              <v-row>
                <v-col class="py-0">
                  <span class="font-weight-bold">구독자 수</span>
                  <br />
                  {{item.subscriber}}
                </v-col>
                <v-divider vertical class="mx-3"></v-divider>
                <v-col class="py-0">
                  <span class="font-weight-bold">총 영상 수</span>
                  <br />
                  {{item.totalVideoCount}}
                </v-col>
                <v-divider vertical class="mx-3"></v-divider>
                <v-col class="py-0">
                  <span class="font-weight-bold">총 영상조회 수</span>
                  <br />
                  {{item.totalViewCount}}
                </v-col>
                <v-spacer></v-spacer>
              </v-row>
            </v-col>
            <v-col cols="2">
              <v-btn
                fab
                :color="setGradeColor(item.grade)"
                style="width: 100%;height: 0;padding-bottom: 50%; padding-top: 50%;"
              >
                <p
                  style="text-align: center;position: absolute;top: 50%;left: 50%;transform: translate(-50%, -50%);color: white;font-size: 150px;"
                >{{item.grade}}</p>
              </v-btn>
            </v-col>
          </v-row>
        </v-container>
      </v-card>
    </v-container>

    <h1>Video</h1>
    <hr />

    <v-container wrap style="background : gray">
      <v-card v-for="(item,i) in searchedvideo.slice(0,3)" :key="i" class="ma-5">
        <v-container>
          <v-row>
            videoName : {{item.videoName }}
            <br />
            videoDescription : {{item.videoDescription }}
            <br />
            videoViewCount : {{item.videoViewCount }}
            <br />
            videoCommentCount : {{item.videoCommentCount }}
            <br />
            good : {{item.good }}
            <br />
            bad : {{item.bad }}
            <br />
            regDate : {{item.regDate }}
            <br />
            ycano : {{item.ycano }}
            <br />
            tags : {{item.tags }}
            <br />
            thumbnail : {{item.thumbnail }}
            <br />
            topic : {{item.topic }}
            <br />
            krCategory : {{item.krCategory }}
            <br />
            enCategory : {{item.enCategory }}
            <br />
          </v-row>
        </v-container>
      </v-card>
    </v-container>

    <h1>News</h1>
    <hr />

    <v-container wrap style="background : gray">
      <v-card v-for="(item,i) in searchednews.slice(0,3)" :key="i" class="ma-5">
        <v-container>
          <v-row>
            newsLink : {{item.newsLink}}
            <br />
            newsTitle : {{item.newsTitle}}
            <br />
            newsDescription : {{item.newsDescription}}
            <br />
            newsDate : {{item.newsDate}}
            <br />
            pressName : {{item.pressName}}
            <br />
            clickCount : {{item.clickCount}}
            <br />
          </v-row>
        </v-container>
      </v-card>
    </v-container>
  </v-container>
</template>


<script>
import http from "../vuex/http-common";
import axios from "axios";

export default {
  components: {},
  name: "searchPage",

  methods: {
    setGradeColor(str) {
      if(typeof(str) == "undefined"){
        return "gray"
      }
      console.log(str)
      if(str.startsWith("S") || str.startsWith("A")){
        return "red"
      }else if(str.startsWith("B")){
        return "orange"
      }else if(str.startsWith("C")){
        return "yellow"
      }else if(str.startsWith("D")){
        return "green"
      }else if(str.startsWith("E")){
        return "blue"
      }else{
        return "gray"
      }
    },
    gotoYoutuberPage: function(yno) {
      this.dialog = false;
      this.$vuetify.goTo(0);
      this.$router.push({ path: "/youtuberPage", query: { yno: yno } });
      this.$vuetify.goTo(0);
    }
  },
  mounted() {
    const youtuberSearch = new Promise((resolve, reject) => {
      http
        .get("/youtuber/search/" + this.$route.query.word)
        .then(response => {
          resolve(response.data.data);
        })
        .catch(err => {
          reject(err);
        });
    });

    const newsSearch = new Promise((resolve, reject) => {
      http
        .get("/news/search/" + this.$route.query.word)
        .then(response => {
          resolve(response.data.data);
        })
        .catch(err => {
          reject(err);
        });
    });

    const videoSearch = new Promise((resolve, reject) => {
      http
        .get("/video/search/" + this.$route.query.word)
        .then(response => {
          resolve(response.data.data);
        })
        .catch(err => {
          reject(err);
        });
    });

    Promise.all([youtuberSearch, newsSearch, videoSearch]).then(
      axios.spread((...responses) => {
        this.searchedyoutuber = responses[0];
        this.searchednews = responses[1];
        this.searchedvideo = responses[2];

        console.log(this.searchedyoutuber);
        console.log(this.searchednews);
        console.log(this.searchedvideo);
      })
    );
  },
  computed: {},
  watch: {
    $route(to, from) {
      if (to.path === "/searchPage") {
        if (to.query.word != from.query.word) {
          const youtuberSearch = new Promise((resolve, reject) => {
            http
              .get("/youtuber/search/" + to.query.word)
              .then(response => {
                resolve(response.data.data);
              })
              .catch(err => {
                reject(err);
              });
          });

          const newsSearch = new Promise((resolve, reject) => {
            http
              .get("/news/search/" + to.query.word)
              .then(response => {
                resolve(response.data.data);
              })
              .catch(err => {
                reject(err);
              });
          });

          const videoSearch = new Promise((resolve, reject) => {
            http
              .get("/video/search/" + to.query.word)
              .then(response => {
                resolve(response.data.data);
              })
              .catch(err => {
                reject(err);
              });
          });
          Promise.all([youtuberSearch, newsSearch, videoSearch]).then(
            axios.spread((...responses) => {
              this.searchedyoutuber = responses[0];
              this.searchednews = responses[1];
              this.searchedvideo = responses[2];

              console.log(this.searchedyoutuber);
              console.log(this.searchednews);
              console.log(this.searchedvideo);
            })
          );
        }
      }
    }
  },
  data() {
    return {
      searchedyoutuber: [],
      searchednews: [],
      searchedvideo: [],
    };
  }
};
</script>

<style scoped>
.circle {
  border-radius: 50%;
}
</style>
