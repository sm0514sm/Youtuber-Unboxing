<template>
  <v-row>
    <v-col cols="12" sm="6">
      <v-hover v-slot:default="{ hover }" open-delay="200">
        <v-card :elevation="hover ? 16 : 2" class="mx-auto" height="350" max-width="350">
          <v-card-text
            class="font-weight-medium mt-12 text-center subtitle-1"
          >Open Delay (Mouse enter)</v-card-text>
        </v-card>
      </v-hover>
    </v-col>

    <v-col cols="12" sm="6">
      <v-hover v-slot:default="{ hover }" close-delay="200">
        <v-card :elevation="hover ? 16 : 2" class="mx-auto" height="350" max-width="350">
          <v-card-text
            class="font-weight-medium mt-12 text-center subtitle-1"
          >Close Delay (Mouse leave)</v-card-text>
        </v-card>
      </v-hover>
    </v-col>
  </v-row>
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
export default {
  name: "TestPage"
};
</script>

<style scoped>
</style>
