<template>
  <v-container>
    <h1>comparePage</h1>
    <!-- header -->
    <v-row>
      <v-col>
        <transition appear name="slide-fade">
          <v-hover v-slot:default="{ hover }" open-delay="100">
            <v-card :elevation="hover ? 7 : 1" shaped class="pa-3 pb-5">
              <v-row>
                <!-- youtuber1 기본정보-->
                <v-col cols="5.5">
                  <v-row>
                    <v-col cols="5" class="pa-3" align="center" justify="center">
                      <v-img class="circle" :src="youtuber1.thumbnails" flat :aspect-ratio="1/1" />
                    </v-col>
                    <v-col cols="7" class="pb-0">
                      <v-row style="height :45%">
                        <v-col>
                          <p class="font-weight-black thin ma-0 headline">{{youtuber1.channelName}}</p>
                        </v-col>
                      </v-row>
                      <v-row>
                        <v-col cols="7">
                          <p
                            class="font-weight-black thin ma-0 headline"
                          >{{youtuber1.publishedDate}}</p>
                        </v-col>
                        <v-col cols="5">
                          <v-btn
                            fab
                            :color="setGradeColor(youtuber1.grade)"
                            style="width: 100%;height: 0;padding-bottom: 50%; padding-top: 50%;"
                          >
                            <p
                              style="text-align: center;position: absolute;top: 50%;left: 50%;transform: translate(-50%, -50%);color: white;font-size: 50px;"
                            >{{youtuber1.grade}}</p>
                          </v-btn>
                        </v-col>
                      </v-row>
                    </v-col>
                  </v-row>
                </v-col>

                <v-col cols="1" align="center">
                  <v-divider vertical></v-divider>
                </v-col>

                <!-- youtuber2 기본정보-->
                <v-col cols="5.5">
                  <v-row>
                    <v-col cols="7" class="pb-0">
                      <v-row style="height :45%">
                        <v-col align="right">
                          <p class="font-weight-black thin ma-0 headline">{{youtuber2.channelName}}</p>
                        </v-col>
                      </v-row>
                      <v-row>
                        <v-col cols="5">
                          <v-btn
                            fab
                            :color="setGradeColor(youtuber2.grade)"
                            style="width: 100%;height: 0;padding-bottom: 50%; padding-top: 50%;"
                          >
                            <p
                              style="text-align: center;position: absolute;top: 50%;left: 50%;transform: translate(-50%, -50%);color: white;font-size: 50px;"
                            >{{youtuber2.grade}}</p>
                          </v-btn>
                        </v-col>
                        <v-col cols="7">
                          <p
                            class="font-weight-black thin ma-0 headline"
                          >{{youtuber2.publishedDate}}</p>
                        </v-col>
                      </v-row>
                    </v-col>
                    <v-col cols="5" class="pa-3" align="center" justify="center">
                      <v-img class="circle" :src="youtuber2.thumbnails" flat :aspect-ratio="1/1" />
                    </v-col>
                  </v-row>
                </v-col>
              </v-row>
            </v-card>
          </v-hover>
        </transition>
      </v-col>
    </v-row>

    <!-- 수치비교 -->
    <v-row>
      <v-col>
        <v-hover v-slot:default="{ hover }" open-delay="100">
          <v-card :elevation="hover ? 7 : 1" class="px-10" shaped>
            <v-row>
              <v-col class="ma-0 mt-5">
                <v-list-item-title class="headline font-weight-black mb-1">수치별비교</v-list-item-title>
                <v-divider></v-divider>
              </v-col>
            </v-row>
            <v-row justify="center" align="center">
              <!-- youtuber1 table -->
              <v-col>
                <v-simple-table wrap="100%">
                  <template v-slot:default>
                    <tbody>
                      <tr v-for="item in youtuber_stat" :key="item.name">
                        <td>{{ item.name }}</td>
                        <td>{{ item.figure1 }}</td>
                      </tr>
                    </tbody>
                  </template>
                </v-simple-table>
              </v-col>
              <!-- 차트 -->
              <v-col cols="6">
                <apexchart
                  type="radar"
                  height="500"
                  :options="chartOptions"
                  :series="series"
                  id="myapexchart"
                  ref="myDiv"
                ></apexchart>
              </v-col>
              <!-- youtuber2 table -->
              <v-col>
                <v-simple-table>
                  <template v-slot:default>
                    <tbody>
                      <tr v-for="item in youtuber_stat" :key="item.name">
                        <td>{{ item.name }}</td>
                        <td>{{ item.figure2 }}</td>
                      </tr>
                    </tbody>
                  </template>
                </v-simple-table>
              </v-col>
            </v-row>
          </v-card>
        </v-hover>
      </v-col>
    </v-row>

    <!-- 기본 수치 비교 -->
    <v-row>
      <v-col cols="6">
        <v-hover v-slot:default="{ hover }" open-delay="100">
          <v-card :elevation="hover ? 7 : 1" class="px-10" shaped>
            <v-row>
              <v-col class="ma-0 mt-5">
                <v-list-item-title class="headline font-weight-black mb-1">기본 수치 비교</v-list-item-title>
                <v-divider></v-divider>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <apexchart
                  type="bar"
                  height="200"
                  :options="getChartOption('subscriber')"
                  :series="subscriberData"
                ></apexchart>
              </v-col>
            </v-row>
          </v-card>
        </v-hover>
      </v-col>
      <v-col cols="6">
        <v-hover v-slot:default="{ hover }" open-delay="100">
          <v-card :elevation="hover ? 7 : 1" class="px-10" shaped>
            <v-row>
              <v-col class="ma-0 mt-5">
                <v-list-item-title class="headline font-weight-black mb-1">수치별비교</v-list-item-title>
                <v-divider></v-divider>
              </v-col>
            </v-row>
          </v-card>
        </v-hover>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Constant from "../vuex/Constant";

export default {
  components: {},
  name: "comparePage",
  beforecreated() {},
  created() {
    this.$vuetify.goTo(0);
    var output = localStorage.getItem("compareYoutuber");
    var arr = JSON.parse(output);
    var list = [];
    list.push(arr[0]);
    list.push(arr[1]);
    this.youtubers = list;
  },

  mounted() {
    this.$store.dispatch(Constant.GET_COMPARE_YOUTUBER, {
      yno1: this.youtubers[0].yno,
      yno2: this.youtubers[1].yno,
      callback: this.callback
    });
  },
  methods: {
    callback(...responses) {
      var youtuber1 = responses[0];
      var youtuber2 = responses[1];
      // var activity4weeks1 = responses[2];
      // var activity4weeks2 = responses[3];
      // var subscriberView1 = responses[4];
      // var subscriberView2 = responses[5];

      //데이터 집어넣기
      this.youtuber1 = youtuber1;
      this.youtuber2 = youtuber2;

      //renderGraph
      var influence1 = this.youtuber1.influence;
      var activity1 = this.youtuber1.activity;
      var viewCountTrend1 = this.youtuber1.viewCountTrend;
      var subscriberCountTrend1 = this.youtuber1.subscriberCountTrend;
      var charm1 = this.youtuber1.charm;

      var influence2 = this.youtuber2.influence;
      var activity2 = this.youtuber2.activity;
      var viewCountTrend2 = this.youtuber2.viewCountTrend;
      var subscriberCountTrend2 = this.youtuber2.subscriberCountTrend;
      var charm2 = this.youtuber2.charm;

      var chart = this.$refs.myDiv;

      chart.appendSeries({
        name: this.youtuber1.channelName,
        data: [
          influence1,
          activity1,
          viewCountTrend1,
          subscriberCountTrend1,
          charm1
        ]
      });
      chart.appendSeries({
        name: this.youtuber2.channelName,
        data: [
          influence2,
          activity2,
          viewCountTrend2,
          subscriberCountTrend2,
          charm2
        ]
      });

      //render table
      this.youtuber_stat = [
        { name: "영향력", figure1: influence1, figure2: influence2 },
        { name: "활동력", figure1: activity1, figure2: activity2 },
        {
          name: "영상조회수증감추이",
          figure1: viewCountTrend1,
          figure2: viewCountTrend2
        },
        {
          name: "구독자증감추이",
          figure1: subscriberCountTrend1,
          figure2: subscriberCountTrend2
        },
        { name: "매력", figure1: charm1, figure2: charm2 }
      ];

      //render basic graph
      this.subscriberData = [
        {
          name: this.youtuber1.channelName,
          data: [this.youtuber1.subscriber]
        },
        {
          name: this.youtuber2.channelName,
          data: [this.youtuber2.subscriber]
        }
      ];
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
    getChartOption(str) {
      return {
        chart: {
          type: "bar",
          height: 150,
          toolbar: {
            show: false
          }
        },
        plotOptions: {
          bar: {
            horizontal: true,
            dataLabels: {
              position: "top"
            }
          }
        },
        dataLabels: {
          enabled: true,
          offsetX: -6,
          style: {
            fontSize: "12px",
            colors: ["#fff"]
          }
        },
        stroke: {
          show: true,
          width: 1,
          colors: ["#fff"]
        },
        xaxis: {
          labels: {
            show: false
          },
          categories: [str]
        },
        yaxis: {},
        legend: {
          show: false
        }
      };
    }
  },
  computed: {},
  data() {
    return {
      youtubers: [],
      youtuber1: {},
      youtuber2: {},
      series: [],
      youtuber_stat: [],
      chartOptions: {
        chart: {
          height: 350,
          type: "radar",
          dropShadow: {
            enabled: true,
            blur: 1,
            left: 1,
            top: 1
          },
          toolbar: {
            show: false
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
            "매력"
          ],
          labels: {
            style: {
              fontSize: "15px",
              colors: ["black", "black", "black", "black", "black"],
              fontFamily: "bold"
            }
          }
        },
        yaxis: {
          show: false,
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
      subscriberData: [],
      totalViewCountData: [],
      totalVideoCountData: []
    };
  }
};
</script>

<style scoped>
.circle {
  border-radius: 50%;
}
.slide-fade-enter-active {
  transition: all 2s ease;
}
.slide-fade-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateY(100px);
  opacity: 0;
}
</style>
