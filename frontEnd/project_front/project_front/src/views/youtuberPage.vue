<template>
  <div>
    <div v-if="loading == 'loading'">
      <v-container>
        <v-row>
          <v-col cols="12">데이터 요청중입니다 ...</v-col>
        </v-row>
        <v-row>
          <v-spacer></v-spacer>
          <v-col>
            <v-progress-circular :size="200" :width="50" color="blue" indeterminate></v-progress-circular>
          </v-col>
          <v-spacer></v-spacer>
        </v-row>
      </v-container>
    </div>
    <!-- <div v-else-if="loading == 'fail'">
      서버와 오류가 발생헀습니다 새로고침(F5)를 눌러주세요.
    </div>-->
    <div v-if="loading == 'success'">
      <!-- header -->
      <v-card flat class="pa-0">
        <v-img :src="youtuber.bannerImageLink" class="py-6 lighten-5"></v-img>
      </v-card>

      <!-- content -->
      <v-container class="pa-0">
        <transition appear name="slide-fade">
          <!--기본정보-->
          <v-card class="my-3" outlined flat>
            <v-container fluid>
              <v-row>
                <!-- thumbnail -->
                <v-col cols="2" class="pa-3">
                  <v-img class="circle" :src="youtuber.thumbnails" flat :aspect-ratio="1/1" />
                </v-col>

                <!-- 기본정보 -->
                <v-col cols="10">
                  <v-row>
                    <v-col class="pb-0">
                      <p class="font-weight-black thin display-3 ma-0">{{youtuber.channelName}}</p>
                    </v-col>
                    <v-col>
                      <v-btn rounded depressed color="#9CDCF0" v-if="true" @click="fav()">임시</v-btn>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col class="pt-0">
                      <span class="font-weight-light">개설일 : {{youtuber.publishedDate}} &nbsp;&nbsp;</span>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col class="ma-0 pa-0">
                      <v-divider class="pa-0 ma-0"></v-divider>
                    </v-col>
                  </v-row>

                  <v-row>
                    <v-col>
                      <span class="font-weight-bold">구독자 수</span>
                      <br />
                      {{youtuber.subscriber}}
                    </v-col>
                    <v-divider vertical class="mx-3"></v-divider>
                    <v-col>
                      <span class="font-weight-bold">총 영상 수</span>
                      <br />
                      {{youtuber.totalVideoCount}}
                    </v-col>
                    <v-divider vertical class="mx-3"></v-divider>
                    <v-col>
                      <span class="font-weight-bold">총 영상조회 수</span>
                      <br />
                      {{youtuber.totalViewCount}}
                    </v-col>
                    <v-spacer></v-spacer>
                  </v-row>
                </v-col>
              </v-row>
            </v-container>
          </v-card>
        </transition>

        <v-row>
          <v-col cols="9">
            <v-col class="pa-0 pb-3">
              <v-card outlined flat>
                <v-row>
                  <v-col class="ma-5">
                    <v-list-item-title class="headline font-weight-black mb-1">능력치</v-list-item-title>
                    <v-divider></v-divider>
                  </v-col>
                </v-row>
                <apexchart
                  type="radar"
                  height="500"
                  :options="chartOptions"
                  :series="mainData"
                  id="myapexchart"
                  ref="myDiv"
                ></apexchart>
              </v-card>
            </v-col>

            <v-col class="pa-0 py-3">
              <v-card outlined flat>
                <v-row>
                  <v-col class="ma-5 pb-0 mb-0">
                    <v-list-item-title class="headline font-weight-black mb-1">각능력치</v-list-item-title>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col>
                    <v-container>
                      <v-tabs v-model="tab" background-color="gray" dark grow>
                        <v-tab>영향력</v-tab>
                        <v-tab>활동력</v-tab>
                        <v-tab>영상조회수증감추이</v-tab>
                        <v-tab>구독자증감추이</v-tab>
                        <v-tab>호감도</v-tab>
                      </v-tabs>

                      <v-tabs-items v-model="tab">
                        <!-- 영향력 -->
                        <v-tab-item>영향력</v-tab-item>

                        <!-- 활동력 -->
                        <v-tab-item>
                          <v-container class="ma-5">
                            <v-row class="mr-10">
                              <p class="display-1">한달간 영상의 수는</p>
                              <p class="display-1" style="color : red">"{{activityDuringMonth}}"</p>
                              <p class="display-1">입니다.</p>
                            </v-row>
                            <v-row class="mr-10">
                              <apexchart
                                :options="activityOptions"
                                :series="activity4weeksData"
                                ref="activityChart"
                                style="width:100%"
                              ></apexchart>
                            </v-row>
                          </v-container>
                        </v-tab-item>

                        <!-- 영상조회수증감추이 -->
                        <v-tab-item>영상조회수증감추이</v-tab-item>

                        <!-- 구독자증감추이 -->
                        <v-tab-item>구독자증감추이</v-tab-item>

                        <!-- 호감도 -->
                        <v-tab-item>
                          <v-container>
                            <v-container class="ma-5">
                              <v-row class="mr-10">최근 10개 동영상 좋아요/싫어요 비율</v-row>
                              <v-row class="mr-10">
                                <v-col cols="2">좋아요</v-col>
                                <v-col cols="8">
                                  <v-progress-linear
                                    background-color="red"
                                    color="blue"
                                    :value="entiregoodratio*100"
                                    height="40"
                                  ></v-progress-linear>
                                  {{entiregoodratio}}
                                </v-col>
                                <v-col cols="2">
                                  <p>싫어요</p>
                                </v-col>
                              </v-row>
                              <v-row class="mr-10">최근 3개의 동영상 좋아요비율</v-row>
                              <v-row class="mr-10">
                                <v-row v-for="(video,i) in recentVideoList" :key="i" class="pa-1">
                                  <v-col cols="12">
                                    <v-card flat color>
                                      <v-row>
                                        <v-col cols="6">
                                          <iframe
                                            :src="String('https://www.youtube.com/embed/')+video.videoID"
                                            frameborder="0"
                                            allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                                            allowfullscreen
                                          ></iframe>
                                        </v-col>
                                        <v-col cols="6">
                                          <v-row>{{video.vno}}</v-row>
                                          <v-row>{{video.regDate}}</v-row>
                                          <v-row>
                                            <v-col
                                              class="pa-1"
                                              cols="2"
                                              style="text-align : center"
                                            >{{video.good}}</v-col>
                                            <v-col class="pa-1">
                                              <v-progress-linear
                                                background-color="red"
                                                color="blue"
                                                :value="video.goodRatio==0 ? 50 : video.goodRatio*100"
                                                height="30"
                                              ></v-progress-linear>
                                            </v-col>
                                            <v-col
                                              class="pa-1"
                                              cols="2"
                                              style="text-align : center"
                                            >{{video.bad}}</v-col>
                                          </v-row>
                                        </v-col>
                                      </v-row>
                                    </v-card>
                                  </v-col>
                                </v-row>
                              </v-row>
                            </v-container>
                          </v-container>
                        </v-tab-item>
                      </v-tabs-items>
                    </v-container>
                  </v-col>
                </v-row>
              </v-card>
            </v-col>
          </v-col>

          <v-col cols="3">
            <v-card outlined flat class="pa-4 pt-0">
              <v-row>
                <v-col class="ma-5 mx-0">
                  <v-list-item-title class="headline font-weight-black mb-1">
                    등급
                    <v-tooltip bottom>
                      <template v-slot:activator="{ on }">
                        <v-icon v-on="on">info</v-icon>
                      </template>
                      <span>등급산정기준은 뭐라뭐라뭘마ㅝ라입니다</span>
                    </v-tooltip>
                  </v-list-item-title>
                  <v-divider></v-divider>
                </v-col>
              </v-row>
              <transition appear name="fade">
                <v-btn
                  fab
                  :color="setGradeColor(youtuber.grade)"
                  style="width: 100%;height: 0;padding-bottom: 50%; padding-top: 50%;"
                >
                  <p
                    style="text-align: center;position: absolute;top: 50%;left: 50%;transform: translate(-50%, -50%);color: white;font-size: 150px;"
                  >{{youtuber.grade}}</p>
                </v-btn>
              </transition>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
// import http from "../vuex/http-common";
import Constant from "../vuex/Constant";
import axios from "axios";

export default {
  components: {},
  name: "youtuberPage",
  beforecreated() {},
  created() {
    this.$vuetify.goTo(0);
    this.loading = "loading";
  },
  mounted() {
    this.$store.dispatch(Constant.GET_YOUTUBER, {
      yno: this.$route.query.yno,
      callback: this.render,
      failCallback: this.failCallback
    });
     axios
            .get("http://70.12.246.59:8000/data/updateStat/" + this.$route.query.yno)
            .then()
            .catch();
  },
  methods: {
    fav(){
      console.log("!")
      console.log(this.$session.get('token'))
    }
    ,
    render(...responses) {
      var youtuber = responses[0];
      var activityDuringMonth = responses[1];
      var activity4weeks = responses[2];
      var charmentiregoodratio = responses[3];
      var charmRecentVideo = responses[4];

      this.youtuber = youtuber;
      this.activityDuringMonth = activityDuringMonth;
      this.entiregoodratio = charmentiregoodratio;
      this.recentVideoList = charmRecentVideo;
      this.activity4weeksData = [
        {
          name: " ",
          data: [
            activity4weeks[0],
            activity4weeks[1],
            activity4weeks[2],
            activity4weeks[3]
          ],
          animation: true
        }
      ];

      var influence = this.youtuber.influence;
      var activity = this.youtuber.activity;
      var viewCountTrend = this.youtuber.viewCountTrend;
      var subscriberCountTrend = this.youtuber.subscriberCountTrend;
      var charm = this.youtuber.charm;
      this.mainData = [
        {
          name: " ",
          data: [
            influence,
            activity,
            viewCountTrend,
            subscriberCountTrend,
            charm
          ]
        }
      ];

        this.loading = "success";

      console.log(this.loading);
      // this.renderMainChart();
      // this.renderActivityChart(activity4weeks);
    },
    renderMainChart() {
      var chart = this.$refs.myDiv;
      var influence = this.youtuber.influence;
      var activity = this.youtuber.activity;
      var viewCountTrend = this.youtuber.viewCountTrend;
      var subscriberCountTrend = this.youtuber.subscriberCountTrend;
      var charm = this.youtuber.charm;

      chart.appendSeries({
        name: " ",
        data: [
          influence,
          activity,
          viewCountTrend,
          subscriberCountTrend,
          charm
        ],
        animation: true
      });
    },
    renderActivityChart(activity4weeks) {
      var chart = this.$refs.activityChart;

      console.log(typeof chart == "undefined");

      this.renderActivityChart(activity4weeks);
      console.log(typeof chart == "undefined");
      chart.appendSeries({
        name: " ",
        data: [
          activity4weeks[0],
          activity4weeks[1],
          activity4weeks[2],
          activity4weeks[3]
        ],
        animation: true
      });
    },
    setGradeColor(str) {
      if (typeof str == "undefined") {
        return "gray";
      }
      if (str.startsWith("S") || str.startsWith("A")) {
        return "red";
      } else if (str.startsWith("B")) {
        return "orange";
      } else if (str.startsWith("C")) {
        return "yellow";
      } else if (str.startsWith("D")) {
        return "green";
      } else if (str.startsWith("E")) {
        return "blue";
      } else {
        return "gray";
      }
    },
    failCallback(err) {
      console.log("****************" + err);
      // this.loading = 'fail';
      console.log(this.loading);
    }
  },
  computed: {},
  data() {
    return {
      youtuber: {},
      mainData: [],
      chartOptions: {
        chart: {
          type: "radar",
          dropShadow: {
            enabled: true,
            blur: 1,
            left: 1,
            top: 1
          }
        },
        title: {},
        stroke: {
          width: 0
        },
        fill: {
          opacity: 0.4
        },
        markers: {
          size: 0
        },
        xaxis: {
          categories: [
            "영향력",
            "활동력",
            "영상조회수증감추이",
            "구독자증감추이",
            "호감도"
          ],
          labels: {
            style: {
              fontSize: "20px",
              colors: ["black", "black", "black", "black", "black"],
              fontFamily: "bold"
            }
          }
        },
        yaxis: {
          show: false,
          max: 100,
          min: 0
        },
        dataLabels: {
          enabled: true,
          background: {
            enabled: true,
            borderRadius: 2
          }
        },
        animations: {
          enabled: false
        }
      },
      activityOptions: {
        series: [],
        chart: {
          type: "line",
          zoom: {
            enabled: false
          }
        },
        dataLabels: {
          enabled: true
        },
        stroke: {
          width: 7,
          curve: "smooth"
        },
        title: {
          text: "동영상",
          align: "center"
        },
        grid: {
          row: {
            colors: ["#f3f3f3", "transparent"],
            opacity: 0.5
          }
        },
        xaxis: {
          categories: ["4주전", "3주전", "2주전", "1주전"]
        }
      },
      activityDuringMonth: 0,
      entiregoodratio: 0,
      recentVideoList: [],
      tab: null,
      activity4weeksData: [],
      loading: "loading"
    };
  }
};
</script>

<style scoped>
.slide-fade-enter-active {
  transition: all 2s ease;
}
.slide-fade-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateX(100px);
  opacity: 0;
}
.circle {
  border-radius: 50%;
}
.jb {
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 3s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
