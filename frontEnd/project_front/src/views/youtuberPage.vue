<template>
  <div>
    <!-- header -->
    <v-card flat class="pa-0">
      <v-img :src="youtuber.bannerImageLink" class="py-6 lighten-5">
      </v-img>
    </v-card>

    <!-- content -->
    <v-container>
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
                :series="series"
                :influence="youtuber.influence"
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
                    <b-tabs content-class="mt-3" fill>
                      <b-tab title="영향력" active>
                        <p class="ma-3">I'm the 영향력 tab</p>
                      </b-tab>
                      <b-tab title="활동력">
                        <p class="ma-3">I'm the 활동력 tab</p>
                      </b-tab>
                      <b-tab title="성장력">
                        <p class="ma-3">I'm the 성장력 tab!</p>
                      </b-tab>
                      <b-tab title="기본수치">
                        <p class="ma-3">I'm the 기본수치 tab!</p>
                      </b-tab>
                      <b-tab title="매력">
                        <p class="ma-3">I'm the 매력 tab!</p>
                      </b-tab>
                    </b-tabs>
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
                <v-list-item-title class="headline font-weight-black mb-1">등급</v-list-item-title>
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

      <!-- mainContainer
      {{this.$route.query.yno}}
      <v-divider></v-divider>
      {{youtuber.yno}}
      <br />
      {{youtuber.channelName}}
      <br />
      {{youtuber.youtuberName}}
      <br />
      {{youtuber.channelDescription}}
      <br />
      {{youtuber.namuwiki}}
      <br />
      {{youtuber.instagram}}
      <br />
      {{youtuber.facebook}}
      <br />
      {{youtuber.thumbnails}}
      <br />
      {{youtuber.publishedDate}}
      <br />
      {{youtuber.subscriber}}
      <br />
      {{youtuber.influence}}-->
    </v-container>
    <!-- <v-btn @click="test('AA')">안녕</v-btn> -->
  </div>
</template>

<script>
import http from "../vuex/http-common";

export default {
  components: {},
  name: "youtuberPage",
  beforecreated() {},
  created() {
    this.$vuetify.goTo(0);
  },
  mounted() {
    http
      .get("/youtuber/" + this.$route.query.yno)
      .then(response => {
        console.log(response.data.data);
        this.youtuber = response.data.data;
        setTimeout(
          function() {
            this.renderGraph();
          }.bind(this),
          1200
        );
      })
      .catch(exp => {
        alert("GET_YOUTUBER 실패하였습니다\n" + exp);
      });
  },
  methods: {
    renderGraph() {
      var chart = this.$refs.myDiv;
      var influence = this.youtuber.influence;
      var activity = this.youtuber.activity;
      var growth = this.youtuber.growth;
      var basicStat = this.youtuber.basicStat;
      var charm = this.youtuber.charm;

      chart.appendSeries({
        name: " ",
        data: [influence, activity, growth, basicStat, charm],
        animation: true
      });
    },
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
    }
  },
  computed: {},
  data() {
    return {
      youtuber: {},
      series: [
        // {
        //   name: " ",
        //   data: [0, 0, 0, 0, 0],
        //   animation: true
        // }
      ],
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
          categories: ["영향력", "활동력", "성장력", "기본수치", "매력"],
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
      }
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
