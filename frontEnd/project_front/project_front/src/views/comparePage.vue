<template>
  <v-container>
    <h1>comparePage</h1>
    <!-- header -->
    <v-row>
      <!-- youtuber1 기본정보-->
      <v-col cols="5">
        <v-row>
          <v-col cols="5" class="pa-3">
            <v-img class="circle" :src="youtuber1.thumbnails" flat :aspect-ratio="1/1" />
          </v-col>
          <v-col cols="7" class="pb-0">
            <p class="font-weight-black thin ma-0 headline">{{youtuber1.channelName}}</p>
          </v-col>
        </v-row>
      </v-col>

      <v-col cols="1"></v-col>
      <v-col cols="1" align-center>
        <v-divider vertical></v-divider>
      </v-col>

      <!-- youtuber2 기본정보-->
      <v-col cols="5">
        <v-row>
          <v-col cols="5" class="pa-3">
            <v-img class="circle" :src="youtuber2.thumbnails" flat :aspect-ratio="1/1" />
          </v-col>
          <v-col cols="7" class="pb-0">
            <p class="font-weight-black thin ma-0 headline">{{youtuber2.channelName}}</p>
          </v-col>
        </v-row>
      </v-col>
    </v-row>

    <!-- 수치비교 -->

    <v-row>
      <!-- youtuber1 table -->
      <v-col>
        <v-simple-table>
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
      youtuber1: this.youtubers[0],
      youtuber2: this.youtubers[1],
      callback: this.renderPage
    });
  },
  methods: {
    renderPage(youtuber1, youtuber2) {
      this.youtuber1 = youtuber1;
      this.youtuber2 = youtuber2;

      //renderGraph
      var chart = this.$refs.myDiv;

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

      chart.appendSeries({
        name: this.youtuber1.channelName,
        data: [influence1, activity1, viewCountTrend1, subscriberCountTrend1, charm1]
      });
      chart.appendSeries({
        name: this.youtuber2.channelName,
        data: [influence2, activity2, viewCountTrend2, subscriberCountTrend2, charm2]
      });

      //render table
      this.youtuber_stat = [
        { name: "영향력", figure1: influence1, figure2: influence2 },
        { name: "활동력", figure1: activity1 , figure2: activity2 },
        { name: "영상조회수증감추이", figure1: viewCountTrend1, figure2: viewCountTrend2  },
        { name: "구독자증감추이", figure1: subscriberCountTrend1, figure2: subscriberCountTrend2 },
        { name: "매력", figure1: charm1 , figure2: charm2 }
      ];

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
          categories: ["영향력", "활동력", "영상조회수증감추이", "구독자증감추이", "매력"],
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
.circle {
  border-radius: 50%;
}
</style>
