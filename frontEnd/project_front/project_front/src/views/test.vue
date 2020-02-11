<template>
  <div id="chart">
    <apexchart type="radar" height="350" :options="chartOptions" :series="series"></apexchart>
  </div>
</template>

<!-- <b-tabs content-class="mt-3" fill>
                      <b-tab title="영향력" active>
                        <v-container class="ma-5">
                          <v-row class="mr-10"></v-row>
                          <v-row class="mr-10"></v-row>
                        </v-container>
                      </b-tab>
                      <b-tab title="활동력">
                        <v-container class="ma-5">
                          <v-row class="mr-10">
                            <p class="display-1">한달간 영상의 수는</p>
                            <p class="display-1" style="color : red">"{{activityDuringMonth}}"</p>
                            <p class="display-1">입니다.</p>
                          </v-row>
                          <v-row class="mr-10">
                            <apexchart
                              :options="activityOptions"
                              :series="series"
                              id="activityChart"
                              ref="activityChart"
                              style="width:100%"
                            ></apexchart>
                          </v-row>
                        </v-container>
                      </b-tab>
                      <b-tab title="영상조회수증감추이">
                        <p class="ma-3">I'm the 영상조회수증감추이 tab!</p>
                      </b-tab>
                      <b-tab title="구독자증감추이">
                        <p class="ma-3">I'm the 구독자증감추이 tab!</p>
                      </b-tab>
                      <b-tab title="호감도">
                        <v-container>
                          <v-container class="ma-5">
                              <v-row class="mr-10">최근 10개 동영상 좋아요/싫어요 비율</v-row>
                              <v-row class="mr-10">
                                <v-col cols="2">
                                  좋아요
                                </v-col>
                                <v-col cols="8">
                                  <v-progress-linear
                                    background-color="blue"
                                    color="red"
                                    :value="entiregoodratio"
                                    height="40"
                                  ></v-progress-linear>
                                </v-col>
                                <v-col cols="2">
                                  <p>싫어요</p>
                                </v-col>
                              </v-row>
                            <v-row class="mr-10">최근 3개의 동영상 좋아요비율</v-row>
                            <v-row class="mr-10">
                              <v-col v-for="(video,i) in recentVideoList" :key="i">{{video.vno}}</v-col>
                            </v-row>
                          </v-container>
                        </v-container>
                      </b-tab>
                    </b-tabs>-->

<script>
import axios from "axios";
export default {
  name: "TestPage",
  methods: {
    test: function() {
      axios
        .get(
          "http://70.12.246.59:8000/data/newYoutuber/https:~~www.youtube.com~channel~UC0M-_02RJqMlGTKUjF1WhJg"
        )
        .then(response => {
          console.log(response);
        })
        .catch(exp => {
          console.log(exp);
        });
    }
  },
  data() {
    return {
      series: [
        {
          name: "Series 1",
          data: [80, 50, 30, 40, 100, 20]
        },
        {
          name: "Series 2",
          data: [20, 30, 40, 80, 20, 80]
        },
        {
          name: "Series 3",
          data: [44, 76, 78, 13, 43, 10]
        }
      ],
      chartOptions: {
        chart: {
          height: 350,
          type: "radar",
          dropShadow: {
            enabled: true,
            blur: 1,
            left: 1,
            top: 1
          }
        },
        title: {
          text: "Radar Chart - Multi Series"
        },
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
          categories: ["2011", "2012", "2013", "2014", "2015", "2016"]
        }
      }
    };
  }
};
</script>

<style scoped>
</style>
