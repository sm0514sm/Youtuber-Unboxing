<template>
  <!-- vuetify를 참고하여 작성하기
  https://vuetifyjs.com/ko/components/api-explorer
  -->

  <div>
    <v-card>
      <v-card-title class="justify-center py-6" style="background-color:#b468ff; height : 300px">
        <v-icon size="70" color="white">mdi-crown</v-icon>
        <span style="text-shadow: 0 0 2px #000;font-size: 2.5em;color:white">RANK</span>
      </v-card-title>
    </v-card>

    <v-container v-scroll="onScroll">
      <v-row>
        <v-col cols="2" class>
          <v-card
            class
            top="50px"
            flat
            outlined
            id="sortCard"
            v-bind:style="{
              position: 'absolute',
              top: sortCardPosition + 'px'
            }"
          >
            <v-container>
              <v-row class="">
                <v-col class="ma-0 pa-0">
                  <h4 class="font-weight-light" style="text-align: center">
                    정렬 기준
                 
                  <v-tooltip top>
                    <template v-slot:activator="{ on }">
                      <v-icon v-on="on" color="blue">mdi-information-outline</v-icon>
                    </template>
                    <span>
                      <v-icon class="mr-2">mdi-star-outline</v-icon>등급 :
                      <b>상위 5%는 SS, 10%는 S, 20%는 A, 50%는 B, 80%는 C, 그 미만은 D등급</b>
                      <br />
                      <v-icon class="mr-2">mdi-earth</v-icon>영향력 :
                      <b>언급수 (커뮤니티 + 뉴스), 구독자수, 영상 총 조회수</b>
                      <br />
                      <v-icon class="mr-2">mdi-newspaper-variant-multiple-outline</v-icon>활동력 :
                      <b>최근 영상 10개의 업로드 주기</b>
                      <br />
                      <v-icon class="mr-2">mdi-heart-multiple-outline</v-icon>호감도 :
                      <b>최근 영상 10개의 좋아요, 싫어요 비율</b>
                    </span>
                  </v-tooltip></h4>
                  <v-divider class="mb-2"></v-divider>
                </v-col>
              </v-row>
              <v-row fluid>
                <v-col class="py-0">
                  <v-radio-group v-model="orderGroup">
                    <v-radio label="구독자순" value="subscriber" checked></v-radio>
                    <v-radio label="등급순" value="grade"></v-radio>
                    <v-radio label="누적조회수" value="totalViewCount"></v-radio>
                    <v-radio label="총영상수" value="totalVideoCount"></v-radio>
                    <v-radio label="영향력" value="influence"></v-radio>
                    <v-radio label="활동력" value="activity"></v-radio>
                    <v-radio label="호감도" value="charm"></v-radio>
                  </v-radio-group>
                </v-col>
              </v-row>
            </v-container>
          </v-card>
        </v-col>

        <!-- 유튜버 리스트 -->
        <v-col cols="10">
          <v-container wrap style="background : white" border class="my-3">
            <v-row class="pt-0 pl-3">
              <v-col>
                <h2 class="font-weight-light mb-1">
                  <v-icon color="#b468ff" size="30">mdi-medal-outline</v-icon>
                  RANK PAGE
                </h2>
                <v-divider class="mb-0 pb-0"></v-divider>
              </v-col>
            </v-row>

            <v-container>
              <v-hover
                v-slot:default="{ hover }"
                open-delay="50"
                v-for="(item, i) in list"
                :key="i"
              >
                <v-card
                  :elevation="hover ? 7 : 0"
                  outlined
                  flat
                  @click="gotoYoutuberPage(item.yno)"
                  class="ma-2"
                  shaped
                >
                  <v-row align="center">
                    <!-- thumbnail -->
                    <v-col class="ma-0 py-5 pl-5 pr-0" cols="2" align="center">
                      <p class="title">{{ i + 1 }}위</p>
                    <!-- </v-col>
                    <v-col class="pr-0" cols="1" align="center"> -->
                      <v-img
                        class="circle"
                        :src="item.thumbnails"
                        flat
                        :aspect-ratio="1 / 1"
                        width="70px"
                      />
                    </v-col>
                    <v-divider vertical class="px-0 ml-0 mr-3"></v-divider>
                    <!-- 유튜버 설명 -->
                    <v-col cols="7" class="pa-1 pr-0 mr-0">
                      <v-row align="center">
                        <v-col cols="12" class="pt-0 pb-1">
                          <p
                            class="font-weight-black thin display-1 ma-0 text-truncate"
                          >{{ item.channelName }}</p>
                        </v-col>
                      </v-row>
                      <v-row>
                        <v-col cols="12" class="pt-0 pb-2">
                          <p
                            class="font-weight-light thin ma-0"
                            style="font-size:13px"
                          >개설일 : {{ item.publishedDate }}</p>
                        </v-col>
                      </v-row>

                      <table style="text-align: center; width: 100%; margin-top: 15px;">
                        <tr id="th">
                          <td>구독자수</td>
                          <td>누적 조회수</td>
                          <td>총 영상수</td>
                          <td>영향력</td>
                          <td>활동력</td>
                          <!-- <td>조회수력</td>
                          <td>구독자력</td> -->
                          <td>호감도</td>
                        </tr>
                        <tr>
                          <td>{{ tc(item.subscriber) }}</td>
                          <td>{{ tc(item.totalViewCount) }}</td>
                          <td>{{ item.totalVideoCount }}</td>
                          <td>{{ item.influence }}</td>
                          <td>{{ item.activity }}</td>
                          <!-- <td>{{ item.viewCountTrend }}</td>
                          <td>{{ item.subscriberCountTrend }}</td> -->
                          <td>{{ item.charm }}</td>
                        </tr>
                      </table>

                      <!-- <v-row>
                        <v-col cols="12" class="py-0">
                          <p class="font-weight-light thin ma-0">
                            구독자 수 :
                            <b>{{ tc(item.subscriber) }}</b> / 누적조회수 :
                            <b>{{ tc(item.totalViewCount) }}</b> / 총영상수 :
                            <b>{{ item.totalVideoCount }}</b>
                          </p>
                        </v-col>
                      </v-row>
                      <v-row>
                        <v-col cols="12" class="py-0">
                          <p class="font-weight-light thin ma-0">
                            영향력 : {{ item.influence }} / 활동력 :
                            {{ item.activity }} / 조회수력 :
                            {{ item.viewCountTrend }} / 구독자력 :
                            {{ item.subscriberCountTrend }} / 호감도 :
                            {{ item.charm }}
                          </p>
                        </v-col>
                      </v-row> -->
                    </v-col>
                    <v-divider vertical class="my-2 ml-5 mr-3 py-4 px-0"></v-divider>
                    <!-- 등급 -->
                    <v-col cols="2" style="text-align: center" class="ma-0">
                      <v-row align="center" class="ma-0">
                        <v-col class="py-1 px-0">
                          <p class="font-weight-bold">&nbsp;&nbsp;GRADE</p>
                        </v-col>
                      </v-row>
                      <v-divider class="ma-0 pa-3"></v-divider>
                      <v-row>
                        <v-col class="">
                          <v-btn
                            class="ma-0 pa-5"
                            fab
                            dark
                            large
                            :color="setGradeColor(item.grade)"
                            height="70px"
                            width="70px"
                          >
                            <v-icon dark>{{ setGrade(item.grade) }}</v-icon>
                          </v-btn>
                        </v-col>
                      </v-row>
                    </v-col>
                  </v-row>
                </v-card>
              </v-hover>
            </v-container>
            <infinite-loading @infinite="infiniteHandler"></infinite-loading>
          </v-container>
        </v-col>
      </v-row>

      <!--youtuber-->
    </v-container>
  </div>
</template>

<script>
import http from "../vuex/http-common";
import tc from "thousands-counter";
import { orderBy } from "natural-orderby";
import InfiniteLoading from "vue-infinite-loading";

export default {
  components: {
    InfiniteLoading
  },
  name: "rankPage",

  methods: {
    setGradeColor(num) {
      if (typeof num == "undefined") {
        return "gray";
      }
      if (num >= 95) {
        return "red";
      } else if (num >= 90) {
        return "orange";
      } else if (num >= 80) {
        return "yellow";
      } else if (num >= 50) {
        return "green";
      } else if (num >= 20) {
        return "blue";
      } else {
        return "gray";
      }
    },
    gotoYoutuberPage: function(yno) {
      this.dialog = false;
      this.$vuetify.goTo(0);
      this.$router.push({ path: "/youtuberPage", query: { yno: yno } });
      this.$vuetify.goTo(0);
    },
    setGrade(num) {
      if (num >= 95) {
        return "SS";
      } else if (num >= 90) {
        return "S";
      } else if (num >= 80) {
        return "A";
      } else if (num >= 50) {
        return "B";
      } else if (num >= 20) {
        return "C";
      } else {
        return "D";
      }
    },
    tc(num) {
      return tc(num);
    },
    callback(list) {
      this.youtubers = list;
      this.youtubers = orderBy(
        this.youtubers,
        [v => v["subscriber"]],
        ["desc"]
      );
      this.list = this.youtubers.slice(0, this.range);
    },
    infiniteHandler($state) {
      setTimeout(() => {
        var tmplist = this.youtubers.slice(
          this.page * this.range,
          this.page * this.range + this.range
        );
        if (tmplist.length > 0) {
          this.page += 1;
          this.list.push(...tmplist);
          $state.loaded();
        } else {
          $state.complete();
        }
      }, 500);
    },
    onScroll() {
      var scroll = window.pageYOffset;
      var fix = 180;
      if (scroll > fix) {
        this.sortCardPosition = 25 + scroll - fix;
      } else {
        this.sortCardPosition = 25;
      }
    },
    failCallback() {
      window.location.reload();
    }
  },
  mounted() {},
  created() {
    http
      .get("/youtuber/all")
      .then(response => {
        console.log(response.data);
        if (response.data.state != "ok") {
          this.failCallback;
        } else {
          this.callback(response.data.data);
        }
      })
      .catch(exp => {
        alert("유튜버 로딩에 실패하였습니다\n" + exp);
      });
    this.orderGroup = "subscriber";
    this.page = 1;
  },
  computed: {},
  watch: {
    orderGroup: function() {
      this.youtubers = orderBy(
        this.youtubers,
        [v => v[this.orderGroup]],
        ["desc"]
      );
      this.list = this.youtubers.slice(0, this.range * this.page);
    }
  },
  data() {
    return {
      youtubers: [],
      list: [],
      orderGroup: {},
      page: 1,
      range: 7,
      sortCardPosition: 20
    };
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Do+Hyeon|Nanum+Gothic|Noto+Sans+KR&display=swap");
* {
  font-family: "Noto Sans KR", sans-serif;
}
.circle {
  border-radius: 50%;
}
td {
  border: 1px solid lightgray;
}
#th {
  background-color: #eeeeee;
}
/* #sortCard{position:absolute;top:100px;} */
</style>
