<template>
  <v-container>
    <!--main하고 합니다-->
    <v-row class="my-5"></v-row>
    <!-- header -->
    <v-row>
      <v-col>
        <transition appear name="slide-fade">
          <v-hover v-slot:default="{ hover }" open-delay="100">
            <v-card :elevation="hover ? 7 : 1" shaped class="pa-3 pb-5">
              <v-row>
                <!-- youtuber1 기본정보-->
                <v-col cols="5.5">
                  <v-card
                    flat
                    elevation="0"
                    :to="{
                      path: 'youtuberPage',
                      query: { yno: youtuber1.yno }
                    }"
                  >
                    <v-row>
                      <v-col cols="5" class="pa-3" align="center" justify="center">
                        <v-img
                          class="circle"
                          :src="youtuber1.thumbnails"
                          flat
                          :aspect-ratio="1 / 1"
                        />
                      </v-col>
                      <v-col cols="7" class="pb-0 pl-3">
                        <v-row style="height :45%">
                          <v-col class="px-0">
                            <p
                              class="font-weight-black thin ma-0 headline"
                            >{{ youtuber1.channelName }}</p>
                          </v-col>
                        </v-row>
                        <v-divider class="ma-0"></v-divider>
                        <v-row>
                          <v-col cols="7">
                            <v-row class="pl-0">
                              <p
                                class="font-weight-black thin ma-0 headline"
                              >{{ youtuber1.publishedDate }}</p>
                            </v-row>
                            <v-row align="center" class="mt-5" style="float: left;">
                              <!-- youtuber -->
                              <v-img
                                width="32px"
                                class="ml-1 mr-1 my-3"
                                src="../assets/youtubeIcon.png"
                                @click="openNewWindow(youtuber1.channelLink)"
                                style="cursor:pointer"
                              />
                              <!-- instagram -->
                              <v-img
                                width="32px"
                                class="mx-1"
                                v-if="otherLinkIcon1[0] != ''"
                                src="../assets/instagramIcon.png"
                                @click="openNewWindow(otherLinkIcon1[0])"
                                style="cursor:pointer"
                              />
                              <!-- twitter -->
                              <v-img
                                width="32px"
                                class="mx-1"
                                v-if="otherLinkIcon1[1] != ''"
                                src="../assets/twitterIcon.png"
                                @click="openNewWindow(otherLinkIcon1[1])"
                                style="cursor:pointer"
                              />
                              <!-- facebook -->
                              <v-img
                                width="32px"
                                class="mx-1"
                                v-if="otherLinkIcon1[2] != ''"
                                src="../assets/facebookIcon.png"
                                @click="openNewWindow(otherLinkIcon1[2])"
                                style="cursor:pointer"
                              />
                              
                            </v-row>
                          </v-col>
                          <v-col cols="5">
                            <v-btn
                              fab
                              :color="setGradeColor(youtuber1.grade)"
                              style="width: 100%;height: 0;padding-bottom: 50%; padding-top: 50%;"
                            >
                              <p
                                style="text-align: center;position: absolute;top: 50%;left: 50%;transform: translate(-50%, -50%);color: white;font-size: 50px;"
                              >{{ setGrade(youtuber1.grade) }}</p>
                            </v-btn>
                          </v-col>
                        </v-row>
                      </v-col>
                    </v-row>
                  </v-card>
                </v-col>

                <v-col cols="1" align="center">
                  <v-divider vertical></v-divider>
                </v-col>

                <!-- youtuber2 기본정보-->
                <v-col cols="5.5">
                  <v-card
                    flat
                    elevation="0"
                    :to="{
                      path: 'youtuberPage',
                      query: { yno: youtuber2.yno }
                    }"
                  >
                    <v-row>
                      <v-col cols="7" class="pb-0">
                        <v-row style="height :45%">
                          <v-col align="right">
                            <p
                              class="font-weight-black thin ma-0 headline"
                            >{{ youtuber2.channelName }}</p>
                          </v-col>
                        </v-row>
                        <v-divider class="ma-0"></v-divider>
                        <v-row>
                          <v-col cols="5">
                            <v-btn
                              fab
                              :color="setGradeColor(youtuber2.grade)"
                              style="width: 100%;height: 0;padding-bottom: 50%; padding-top: 50%;"
                            >
                              <p
                                style="text-align: center;position: absolute;top: 50%;left: 50%;transform: translate(-50%, -50%);color: white;font-size: 50px; text-align: right;"
                              >{{ setGrade(youtuber2.grade) }}</p>
                            </v-btn>
                          </v-col>
                          <v-col cols="7">
                            <v-row class="pl-7">
                              <p
                                class="font-weight-black thin ma-0 headline"
                                style="text-align='right'"
                              >{{ youtuber2.publishedDate }}</p>
                            </v-row>
                            <v-row align="center" class="mt-5" style="float: left;">
                              <!-- youtuber -->
                              <v-img
                                width="32px"
                                class="ml-1 mr-1 my-3"
                                src="../assets/youtubeIcon.png"
                                @click="openNewWindow(youtuber2.channelLink)"
                                style="cursor:pointer"
                              />
                              <!-- instagram -->
                              <v-img
                                width="32px"
                                class="mx-1"
                                v-if="otherLinkIcon2[0] != ''"
                                src="../assets/instagramIcon.png"
                                @click="openNewWindow(otherLinkIcon2[0])"
                                style="cursor:pointer"
                              />
                              <!-- twitter -->
                              <v-img
                                width="32px"
                                class="mx-1"
                                v-if="otherLinkIcon2[1] != ''"
                                src="../assets/twitterIcon.png"
                                @click="openNewWindow(otherLinkIcon2[1])"
                                style="cursor:pointer"
                              />
                              <!-- facebook -->
                              <v-img
                                width="32px"
                                class="mx-1"
                                v-if="otherLinkIcon2[2] != ''"
                                src="../assets/facebookIcon.png"
                                @click="openNewWindow(otherLinkIcon2[2])"
                                style="cursor:pointer"
                              />
                              
                            </v-row>
                          </v-col>
                        </v-row>
                      </v-col>
                      <v-col cols="5" class="pa-3" align="center" justify="center">
                        <v-img
                          class="circle"
                          :src="youtuber2.thumbnails"
                          flat
                          :aspect-ratio="1 / 1"
                        />
                      </v-col>
                    </v-row>
                  </v-card>
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
              <v-col class="ma-0 mt-5 pb-0">
                <v-list-item-title class="headline font-weight-black mb-1">수치별 비교</v-list-item-title>
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

    <v-row>
      <!-- 기본 수치 비교 -->
      <v-col cols="6">
        <v-hover v-slot:default="{ hover }" open-delay="100">
          <v-card :elevation="hover ? 7 : 1" class="px-10" shaped>
            <v-row>
              <v-col class="ma-0 mt-5 pb-0">
                <v-list-item-title class="headline font-weight-black mb-1">기본 수치 비교</v-list-item-title>
                <v-divider></v-divider>
              </v-col>
            </v-row>
            <!--구독자 -->
            <v-row>
              <v-col class="py-0">
                <apexchart
                  type="bar"
                  height="200"
                  :options="getChartOption('구독자')"
                  :series="subscriberData"
                ></apexchart>
              </v-col>
            </v-row>
            <!-- totalViewCount -->
            <v-row>
              <v-col class="py-0">
                <apexchart
                  type="bar"
                  height="200"
                  :options="getChartOption('총영상조회수')"
                  :series="totalViewCountData"
                ></apexchart>
              </v-col>
            </v-row>
            <!-- totalVideoCount -->
            <v-row>
              <v-col class="py-0">
                <apexchart
                  type="bar"
                  height="200"
                  :options="getChartOption('총영상수')"
                  :series="totalVideoCountData"
                ></apexchart>
              </v-col>
            </v-row>
          </v-card>
        </v-hover>
      </v-col>

      <v-col cols="6">
        <v-hover v-slot:default="{ hover }" open-delay="100">
          <v-card :elevation="hover ? 7 : 1" class="px-10" shaped>
            <v-divider></v-divider>
            <v-list-item-title class="headline font-weight-black mb-1">분야별 수치 비교</v-list-item-title>
            <v-divider></v-divider>
            <v-row>
              <v-col class="py-0">
                <v-badge color="#269ffb" bordered overlap>
                  <v-avatar>
                    <v-img :src="youtuber1.thumbnails"></v-img>
                  </v-avatar>
                </v-badge>
                <v-chip
                  style="border-width: medium"
                  class="ma-2"
                  color="#269ffb"
                  outlined
                  pill
                  text-color="black"
                >
                  <b>{{youtuber1.channelName | truncate(10,"..")}}</b>
                </v-chip>
              </v-col>
              <v-col class="py-0">
                <v-badge color="#26e7a5" bordered overlap>
                  <v-avatar>
                    <v-img :src="youtuber2.thumbnails"></v-img>
                  </v-avatar>
                </v-badge>
                <v-chip
                  style="border-width: medium"
                  class="ma-2"
                  color="#26e7a5"
                  outlined
                  pill
                  text-color="black"
                >
                  <b>{{youtuber2.channelName | truncate(10,"..")}}</b>
                </v-chip>
              </v-col>
            </v-row>

            <v-row>
              <v-col>
                <v-row v-if="status.y1_sub">
                  <v-chip
                    class="ma-2"
                    color="#26c3fb"
                    outlined
                    text-color="black"
                    style="border-width: medium"
                  >
                    <v-icon left color="#26c3fb">mdi-account-multiple</v-icon>
                    <b>조회수 증감률 {{ status.sub_stat }}%</b>
                    <v-icon color="#26c3fb">mdi-arrow-up-thick</v-icon>
                  </v-chip>
                </v-row>
                <v-row v-if="status.y1_view">
                  <v-chip
                    class="ma-2"
                    color="#26b1fb"
                    outlined
                    text-color="black"
                    style="border-width: medium"
                  >
                    <v-icon left color="#26b1fb">mdi-animation-play</v-icon>
                    <b>구독자 증감률 {{ status.view_stat }}%</b>
                    <v-icon color="#26b1fb">mdi-arrow-up-thick</v-icon>
                  </v-chip>
                </v-row>
                <v-row v-if="status.y1_video">
                  <v-chip
                    class="ma-2"
                    color="#269ffb"
                    outlined
                    text-color="black"
                    style="border-width: medium"
                  >
                    <v-icon left color="#269ffb">mdi-youtube-subscription</v-icon>
                    <b>영상수 {{ status.video_stat }}%</b>
                    <v-icon color="#269ffb">mdi-arrow-up-thick</v-icon>
                  </v-chip>
                </v-row>

                <v-row v-if="status.y1_charm">
                  <v-chip
                    class="ma-2"
                    color="#268dfb"
                    outlined
                    text-color="black"
                    style="border-width: medium"
                  >
                    <v-icon left color="#268dfb">mdi-heart-multiple</v-icon>
                    <b>호감도 {{ status.charm_stat }}%</b>
                    <v-icon color="#268dfb">mdi-arrow-up-thick</v-icon>
                  </v-chip>
                </v-row>
                <v-row v-if="status.y1_influence">
                  <v-chip
                    class="ma-2"
                    color="#267cfb"
                    outlined
                    text-color="black"
                    style="border-width: medium"
                  >
                    <v-icon left color="#267cfb">mdi-earth</v-icon>
                    <b>영향력 {{ status.influence_stat }}%</b>
                    <v-icon color="#267cfb">mdi-arrow-up-thick</v-icon>
                  </v-chip>
                </v-row>
                <v-row v-if="status.y1_activity">
                  <v-chip
                    class="ma-2"
                    color="#266afb"
                    outlined
                    text-color="black"
                    style="border-width: medium"
                  >
                    <v-icon left color="#266afb">mdi-newspaper-variant-multiple</v-icon>
                    <b>활동력 {{ status.activity_stat }}%</b>
                    <v-icon color="#266afb">mdi-arrow-up-thick</v-icon>
                  </v-chip>
                </v-row>
              </v-col>

              <v-divider vertical class="mr-5"></v-divider>

              <v-col>
                <v-row v-if="status.y2_sub">
                  <v-chip
                    class="ma-2"
                    color="#26e785"
                    text-color="black"
                    outlined
                    style="border-width: medium"
                  >
                    <v-icon left color="#26e785">mdi-account-multiple</v-icon>
                    <b>조회수 증감률 {{ status.sub_stat }}%</b>
                    <v-icon color="#26e785">mdi-arrow-up-thick</v-icon>
                  </v-chip>
                </v-row>
                <v-row v-if="status.y2_view">
                  <v-chip
                    class="ma-2"
                    color="#26e795"
                    text-color="black"
                    outlined
                    style="border-width: medium"
                  >
                    <v-icon left color="#26e795">mdi-animation-play</v-icon>
                    <b>구독자 증감률 {{ status.view_stat }}%</b>
                    <v-icon color="#26e795">mdi-arrow-up-thick</v-icon>
                  </v-chip>
                </v-row>
                <v-row v-if="status.y2_video">
                  <v-chip
                    class="ma-2"
                    color="#26e7a5"
                    text-color="black"
                    outlined
                    style="border-width: medium"
                  >
                    <v-icon left color="#26e7a5">mdi-youtube-subscription</v-icon>
                    <b>영상수 {{ status.video_stat }}%</b>
                    <v-icon color="#26e7a5">mdi-arrow-up-thick</v-icon>
                  </v-chip>
                </v-row>

                <v-row v-if="status.y2_charm">
                  <v-chip
                    class="ma-2"
                    color="#26e7b5"
                    text-color="black"
                    outlined
                    style="border-width: medium"
                  >
                    <v-icon left color="#26e7b5">mdi-heart-multiple</v-icon>
                    <b>호감도 {{ status.charm_stat }}%</b>
                    <v-icon color="#26e7b5">mdi-arrow-up-thick</v-icon>
                  </v-chip>
                </v-row>
                <v-row v-if="status.y2_influence">
                  <v-chip
                    class="ma-2"
                    color="#26e7c5"
                    text-color="black"
                    outlined
                    style="border-width: medium"
                  >
                    <v-icon left color="#26e7c5">mdi-earth</v-icon>
                    <b>영향력 {{ status.influence_stat }}%</b>
                    <v-icon color="#26e7c5">mdi-arrow-up-thick</v-icon>
                  </v-chip>
                </v-row>
                <v-row v-if="status.y2_activity">
                  <v-chip
                    class="ma-2"
                    color="#26e7d5"
                    text-color="black"
                    outlined
                    style="border-width: medium"
                  >
                    <v-icon left color="#26e7d5">mdi-newspaper-variant-multiple</v-icon>
                    <b>활동력 {{ status.activity_stat }}%</b>
                    <v-icon color="#26e7d5">mdi-arrow-up-thick</v-icon>
                  </v-chip>
                </v-row>
              </v-col>
            </v-row>
            <v-divider></v-divider>

            <v-list-item-title class="headline font-weight-black mb-1">종합 비교</v-list-item-title>
            <v-row>
              <v-badge v-if="!status.same_grade" :color="status.color" bordered overlap size="125">
                <v-card>
                  <div class="d-flex flex-no-wrap justify-space-between">
                    <div>
                      <v-card-title class="headline">
                        <div>
                          <v-chip
                            class="ma-2 pa-1 pr-2"
                            color="yellow"
                            outlined
                            pill
                            text-color="black"
                            style="border-width: medium"
                          >
                            <v-icon color="yellow">mdi-crown</v-icon>
                            <b>{{ status.winner }}</b>
                          </v-chip>채널이
                        </div>
                        <br />
                        <div>
                          총
                          <v-chip
                            class="ma-2"
                            color="indigo darken-3"
                            outlined
                            style="border-width: medium"
                          >
                            <v-icon left>mdi-fire</v-icon>
                            <b>{{ status.stat }}%</b>
                          </v-chip>우위에 있습니다.
                        </div>
                      </v-card-title>
                    </div>

                    <v-avatar class="ma-3" size="125">
                      <v-img :src="status.thumbnail"></v-img>
                    </v-avatar>
                  </div>
                </v-card>
              </v-badge>
              <v-card v-if="status.same_grade" color="#F5F5F5">
                <v-card-title class="justify-center" align="center">
                  <v-badge color="#269ffb" bordered overlap>
                    <v-avatar size="75">
                      <v-img :src="youtuber1.thumbnails"></v-img>
                    </v-avatar>
                  </v-badge>
                  <v-chip class="ma-2">
                    <v-icon>mdi-equal</v-icon>
                  </v-chip>
                  <v-badge color="#26e7a5" bordered overlap>
                    <v-avatar size="75" border>
                      <v-img :src="youtuber2.thumbnails"></v-img>
                    </v-avatar>
                  </v-badge>
                </v-card-title>
                <v-card-title class="headline">채널 종합 수치가 동률 입니다</v-card-title>
              </v-card>
            </v-row>
            <v-divider></v-divider>
          </v-card>
        </v-hover>
      </v-col>
    </v-row>

    <!-- 총영상수 주기 -->
    <v-row>
      <v-col>
        <v-hover v-slot:default="{ hover }" open-delay="100">
          <v-card :elevation="hover ? 7 : 1" class="px-10" shaped>
            <v-row>
              <v-col class="ma-0 mt-5">
                <v-list-item-title class="headline font-weight-black mb-1">영상수 주기</v-list-item-title>
                <v-divider></v-divider>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <apexchart height="200" :options="videoPeriodOptions" :series="videoPeriodData"></apexchart>
              </v-col>
            </v-row>
          </v-card>
        </v-hover>
      </v-col>
    </v-row>

    <!-- 구독자 추이 -->
    <v-row>
      <v-col>
        <v-hover v-slot:default="{ hover }" open-delay="100">
          <v-card :elevation="hover ? 7 : 1" class="px-10" shaped>
            <v-row>
              <v-col class="ma-0 mt-5">
                <v-list-item-title class="headline font-weight-black mb-1">구독자 추이</v-list-item-title>
                <v-divider></v-divider>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <apexchart
                  height="200"
                  :options="subscriberPeriodOptions"
                  :series="subscriberPeriodData"
                ></apexchart>
              </v-col>
            </v-row>
          </v-card>
        </v-hover>
      </v-col>
    </v-row>

    <!-- 총조회수추이 -->
    <v-row>
      <v-col>
        <v-hover v-slot:default="{ hover }" open-delay="100">
          <v-card :elevation="hover ? 7 : 1" class="px-10" shaped>
            <v-row>
              <v-col class="ma-0 mt-5">
                <v-list-item-title class="headline font-weight-black mb-1">총조회수 추이</v-list-item-title>
                <v-divider></v-divider>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <apexchart
                  height="200"
                  :options="totalViewPeriodOptions"
                  :series="totalViewPeriodData"
                ></apexchart>
              </v-col>
            </v-row>
          </v-card>
        </v-hover>
      </v-col>
    </v-row>

    <!-- 누적조회수 증감 추이 -->
    <v-row>
      <v-col>
        <v-hover v-slot:default="{ hover }" open-delay="100">
          <v-card :elevation="hover ? 7 : 1" class="px-10" shaped>
            <v-row>
              <v-col class="ma-0 mt-5">
                <v-list-item-title class="headline font-weight-black mb-1">조회수 증가 추이</v-list-item-title>
                <v-divider></v-divider>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <apexchart height="200" :options="totalViewDiffOptions" :series="totalViewDiffData"></apexchart>
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
import tc from "thousands-counter";

export default {
  components: {},
  name: "comparePage",
  beforecreated() {},
  created() {
    this.$vuetify.goTo(0);
    var output = localStorage.getItem("compareYoutuber");
    var arr = JSON.parse(output);
    if (arr.length != 2) {
      this.istwoyoutuber = false;
      this.$router.push({ path: "notFound" });
      return;
    }
    var list = [];
    list.push(arr[0]);
    list.push(arr[1]);
    this.youtubers = list;
  },

  mounted() {
    this.$store.dispatch(Constant.GET_COMPARE_YOUTUBER, {
      yno1: this.youtubers[0].yno,
      yno2: this.youtubers[1].yno,
      callback: this.callback,
      failCallback: this.failCallback
    });
  },
  methods: {
    check() {
      console.log(this.youtuber1);
      console.log(this.youtuber2);

      if (this.youtuber1.grade > this.youtuber2.grade) {
        this.status["winner"] = this.youtuber1.channelName;
        this.status["thumbnail"] = this.youtuber1.thumbnails;
        this.status["color"] = "#269ffb";
        this.status["same_grade"] = false;
        this.status["stat"] = Math.round(
          ((this.youtuber1.grade - this.youtuber2.grade) /
            this.youtuber2.grade) *
            100
        );
      } else if (this.youtuber1.grade == this.youtuber2.grade) {
        this.status["same_grade"] = true;
      } else {
        this.status["winner"] = this.youtuber2.channelName;
        this.status["thumbnail"] = this.youtuber2.thumbnails;
        this.status["color"] = "#26e7a5";
        this.status["same_grade"] = false;
        this.status["stat"] = Math.round(
          ((this.youtuber2.grade - this.youtuber1.grade) /
            this.youtuber1.grade) *
            100
        );
      }

      if (this.youtuber1.viewCountTrend > this.youtuber2.viewCountTrend) {
        this.status["y1_sub"] = true;
        this.status["y2_sub"] = false;
        this.status["sub_stat"] = Math.round(
          ((this.youtuber1.viewCountTrend - this.youtuber2.viewCountTrend) /
            this.youtuber2.viewCountTrend) *
            100
        );
      } else if (
        this.youtuber1.viewCountTrend == this.youtuber2.viewCountTrend
      ) {
        this.status["y1_sub"] = false;
        this.status["y2_sub"] = false;
        this.status["sub_stat"] = 0;
      } else {
        this.status["y1_sub"] = false;
        this.status["y2_sub"] = true;
        this.status["sub_stat"] = Math.round(
          ((this.youtuber2.viewCountTrend - this.youtuber1.viewCountTrend) /
            this.youtuber1.viewCountTrend) *
            100
        );
      }
      if (this.youtuber1.totalVideoCount > this.youtuber2.totalVideoCount) {
        this.status["y1_video"] = true;
        this.status["y2_video"] = false;
        this.status["video_stat"] = Math.round(
          ((this.youtuber1.totalVideoCount - this.youtuber2.totalVideoCount) /
            this.youtuber2.totalVideoCount) *
            100
        );
      } else if (
        this.youtuber1.totalViewCount == this.youtuber2.totalViewCount
      ) {
        this.status["y1_video"] = false;
        this.status["y2_video"] = false;
        this.status["video_stat"] = 0;
      } else {
        this.status["y1_video"] = false;
        this.status["y2_video"] = true;
        this.status["video_stat"] = Math.round(
          ((this.youtuber2.totalVideoCount - this.youtuber1.totalVideoCount) /
            this.youtuber1.totalVideoCount) *
            100
        );
      }
      if (
        this.youtuber1.subscriberCountTrend >
        this.youtuber2.subscriberCountTrend
      ) {
        this.status["y1_view"] = true;
        this.status["y2_view"] = false;
        this.status["view_stat"] = Math.round(
          ((this.youtuber1.subscriberCountTrend -
            this.youtuber2.subscriberCountTrend) /
            this.youtuber2.subscriberCountTrend) *
            100
        );
      } else if (
        this.youtuber1.subscriberCountTrend ==
        this.youtuber2.subscriberCountTrend
      ) {
        this.status["y1_view"] = false;
        this.status["y2_view"] = false;
        this.status["view_stat"] = 0;
      } else {
        this.status["y1_view"] = false;
        this.status["y2_view"] = true;
        this.status["view_stat"] = Math.round(
          ((this.youtuber2.subscriberCountTrend -
            this.youtuber1.subscriberCountTrend) /
            this.youtuber1.subscriberCountTrend) *
            100
        );
      }

      if (this.youtuber1.charm > this.youtuber2.charm) {
        this.status["y1_charm"] = true;
        this.status["y2_charm"] = false;
        this.status["charm_stat"] = Math.round(
          ((this.youtuber1.charm - this.youtuber2.charm) /
            this.youtuber2.charm) *
            100
        );
      } else if (this.youtuber1.charm == this.youtuber2.charm) {
        this.status["y1_charm"] = false;
        this.status["y2_charm"] = false;
        this.status["charm_stat"] = 0;
      } else {
        this.status["y1_charm"] = false;
        this.status["y2_charm"] = true;
        this.status["charm_stat"] = Math.round(
          ((this.youtuber2.charm - this.youtuber1.charm) /
            this.youtuber1.charm) *
            100
        );
      }
      if (this.youtuber1.influence > this.youtuber2.influence) {
        this.status["y1_influence"] = true;
        this.status["y2_influence"] = false;
        this.status["influence_stat"] = Math.round(
          ((this.youtuber1.influence - this.youtuber2.influence) /
            this.youtuber2.influence) *
            100
        );
      } else if (this.youtuber1.influence == this.youtuber2.influence) {
        this.status["y1_influence"] = false;
        this.status["y2_influence"] = false;
        this.status["influence_stat"] = 0;
      } else {
        this.status["y1_influence"] = false;
        this.status["y2_influence"] = true;
        this.status["influence_stat"] = Math.round(
          ((this.youtuber2.influence - this.youtuber1.influence) /
            this.youtuber1.influence) *
            100
        );
      }

      if (this.youtuber1.activity > this.youtuber2.activity) {
        this.status["y1_activity"] = true;
        this.status["y2_activity"] = false;
        this.status["activity_stat"] = Math.round(
          ((this.youtuber1.activity - this.youtuber2.activity) /
            this.youtuber2.activity) *
            100
        );
      } else if (this.youtuber1.activity == this.youtuber2.activity) {
        this.status["y1_activity"] = false;
        this.status["y2_activity"] = false;
        this.status["activity_stat"] = 0;
      } else {
        this.status["y1_activity"] = false;
        this.status["y2_activity"] = true;
        this.status["activity_stat"] = Math.round(
          ((this.youtuber2.activity - this.youtuber1.activity) /
            this.youtuber1.activity) *
            100
        );
      }

      console.log(this.status);
    },
    callback(...responses) {
      var youtuber1 = responses[0];
      var youtuber2 = responses[1];
      var activity25weeks1 = responses[2];
      var activity25weeks2 = responses[3];
      var subscriberView1 = responses[4];
      var subscriberView2 = responses[5];

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
      this.totalViewCountData = [
        {
          name: this.youtuber1.channelName,
          data: [this.youtuber1.totalViewCount]
        },
        {
          name: this.youtuber2.channelName,
          data: [this.youtuber2.totalViewCount]
        }
      ];
      this.totalVideoCountData = [
        {
          name: this.youtuber1.channelName,
          data: [this.youtuber1.totalVideoCount]
        },
        {
          name: this.youtuber2.channelName,
          data: [this.youtuber2.totalVideoCount]
        }
      ];

      //영상수주기
      this.videoPeriodData = [
        {
          name: this.youtuber1.channelName,
          data: activity25weeks1
        },
        {
          name: this.youtuber2.channelName,
          data: activity25weeks2
        }
      ];
      for (let index = activity25weeks1.length - 1; index > 0; index--) {
        this.videoPeriodOptions["xaxis"]["categories"].push(index + "주전");
      }

      //구독자 추이
      this.subscriberPeriodData = [
        {
          name: this.youtuber1.channelName,
          data: []
        },
        {
          name: this.youtuber2.channelName,
          data: []
        }
      ];

      var max = Math.max(subscriberView1.length, subscriberView2.length);
      for (let index = 0; index < max; index++) {
        
        if (
          subscriberView1[index] != undefined &&
          !this.subscriberPeriodOptions["xaxis"]["categories"].includes(
            subscriberView1[index].recordDate
          )
        ) {
          this.subscriberPeriodOptions["xaxis"]["categories"].push(
            subscriberView1[index].recordDate
          );
        }

        if (
          subscriberView2[index] != undefined &&
          !this.subscriberPeriodOptions["xaxis"]["categories"].includes(
            subscriberView2[index].recordDate
          )
        ) {
          this.subscriberPeriodOptions["xaxis"]["categories"].push(
            subscriberView2[index].recordDate
          );
        }
      }


      this.subscriberPeriodOptions["xaxis"]["categories"].sort();

      var i = 0;
      for (let index = 0; index < max; index++) {
        
        if (
          subscriberView1[i] != undefined && 
          this.subscriberPeriodOptions["xaxis"]["categories"][index] ==
          subscriberView1[i].recordDate
        ) {
          this.subscriberPeriodData[0]["data"].push(
            subscriberView1[i].pointSubscriber
          );
          i++;
        } else {
          this.subscriberPeriodData[0]["data"].push(null);
        }
      }


      i = 0;
      console.log(subscriberView2[i])
      for (let index = 0; index < max; index++) {
        if (
          subscriberView2[i] != undefined && 
          this.subscriberPeriodOptions["xaxis"]["categories"][index] ==
          subscriberView2[i].recordDate
        ) {
          this.subscriberPeriodData[1]["data"].push(
            subscriberView2[i].pointSubscriber
          );
          i++;
        } else {
          this.subscriberPeriodData[1]["data"].push(null);
        }
      }


      //누적조회수추이
      this.totalViewPeriodData = [
        {
          name: this.youtuber1.channelName,
          data: []
        },
        {
          name: this.youtuber2.channelName,
          data: []
        }
      ];


      for (let index = 0; index < max; index++) {
        if (
          subscriberView1[index] != undefined &&
          !this.totalViewPeriodOptions["xaxis"]["categories"].includes(
            subscriberView1[index].recordDate
          )
        ) {
          this.totalViewPeriodOptions["xaxis"]["categories"].push(
            subscriberView1[index].recordDate
          );
        }

        if (
          subscriberView2[index] != undefined &&
          !this.totalViewPeriodOptions["xaxis"]["categories"].includes(
            subscriberView2[index].recordDate
          )
        ) {
          this.totalViewPeriodOptions["xaxis"]["categories"].push(
            subscriberView2[index].recordDate
          );
        }
      }

      this.totalViewPeriodOptions["xaxis"]["categories"].sort();

      i = 0;
      for (let index = 0; index < max; index++) {
        
        if (
          subscriberView1[i] != undefined && 
          this.totalViewPeriodOptions["xaxis"]["categories"][index] ==
          subscriberView1[i].recordDate
        ) {
          this.totalViewPeriodData[0]["data"].push(
            subscriberView1[i].pointView
          );
          i++;
        } else {
          this.totalViewPeriodData[0]["data"].push(null);
        }
      }


      i = 0;
      for (let index = 0; index < max; index++) {
        if (
          subscriberView2[i] != undefined && 
          this.totalViewPeriodOptions["xaxis"]["categories"][index] ==
          subscriberView2[i].recordDate
        ) {
          this.totalViewPeriodData[1]["data"].push(
            subscriberView2[i].pointView
          );
          i++;
        } else {
          this.totalViewPeriodData[1]["data"].push(null);
        }
      }

      console.log(this.totalViewPeriodOptions["xaxis"]["categories"]);

      // viewDiff
      this.totalViewDiffData = [
        {
          name: this.youtuber1.channelName,
          data: []
        },
        {
          name: this.youtuber2.channelName,
          data: []
        }
      ];

      for (let index = 0; index < max; index++) {
        if (
          subscriberView1[index] != undefined &&
          !this.totalViewDiffOptions["xaxis"]["categories"].includes(
            subscriberView1[index].recordDate
          )
        ) {
          this.totalViewDiffOptions["xaxis"]["categories"].push(
            subscriberView1[index].recordDate
          );
        }

        if (
          subscriberView2[index] != undefined &&
          !this.totalViewDiffOptions["xaxis"]["categories"].includes(
            subscriberView2[index].recordDate
          )
        ) {
          this.totalViewDiffOptions["xaxis"]["categories"].push(
            subscriberView2[index].recordDate
          );
        }
      }

      this.totalViewDiffOptions["xaxis"]["categories"].sort();

      i = 0;
      for (let index = 0; index < max; index++) {
        if (
          subscriberView1[i] != undefined && 
          this.totalViewDiffOptions["xaxis"]["categories"][index] ==
          subscriberView1[i].recordDate
        ) {
          this.totalViewDiffData[0]["data"].push(subscriberView1[i].difView);
          i++;
        } else {
          this.totalViewDiffData[0]["data"].push(null);
        }
      }

      i = 0;
      for (let index = 0; index < max; index++) {
        if (
          subscriberView2[i] != undefined && 
          this.totalViewDiffOptions["xaxis"]["categories"][index] ==
          subscriberView2[i].recordDate
        ) {
          this.totalViewDiffData[1]["data"].push(subscriberView2[i].difView);
          i++;
        } else {
          this.totalViewDiffData[1]["data"].push(null);
        }
      }


      // for (let index = 0; index < subscriberView1.length; index++) {
      //   this.totalViewDiffData[0]["data"].push(subscriberView1[index].difView);
      //   this.totalViewDiffData[1]["data"].push(subscriberView2[index].difView);
      //   this.totalViewDiffOptions["xaxis"]["categories"].push(
      //     subscriberView1[index].recordDate.substring(5, 10)
      //   );
      // }

      //otherLink
      this.makeOtherLinkIcon();

      this.check();
    },
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
    getChartOption(str) {
      if (str == "총영상수") {
        return {
          chart: {
            type: "bar",
            height: 180,
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
            },
            formatter: value => {
              return tc(value);
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
          yaxis: {
            show: false
          },
          legend: {
            show: true
          },
          title: {
            text: str,
            align: "center",
            margin: 0,
            offsetX: 0,
            offsetY: 0,
            floating: false,
            style: {
              fontSize: "17px",
              fontWeight: "bold",
              color: "black"
            }
          },
          tooltip: {
            y: {
              formatter: function(x) {
                return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
              }
            }
          }
        };
      } else {
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
            },
            formatter: value => {
              return tc(value);
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
          yaxis: {
            show: false
          },
          legend: {
            show: false
          },
          title: {
            text: str,
            align: "center",
            margin: 0,
            offsetX: 0,
            offsetY: 0,
            floating: false,
            style: {
              fontSize: "17px",
              fontWeight: "bold",
              color: "black"
            }
          },
          tooltip: {
            y: {
              formatter: function(x) {
                return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
              }
            }
          }
        };
      }
    },
    makeOtherLinkIcon() {
      var site = ["instagram", "twitter", "facebook", "tiktok"];
      var y1 = this.youtuber1;
      var link1 = [
        y1.otherLink1, 
        y1.otherLink2,
        y1.otherLink3,
        y1.otherLink4,
        y1.otherLink5
      ];

      this.otherLinkIcon1 = ["", "", "", ""];

      for (let i = 0; i < link1.length; i++) {
        for (let j = 0; j < site.length; j++) {
          if (link1[i].indexOf(site[j]) != -1) {
            this.otherLinkIcon1[j] = link1[i];
            break;
          }
        }
      }

      var y2 = this.youtuber2;
      var link2 = [
        y2.otherLink1,
        y2.otherLink2,
        y2.otherLink3,
        y2.otherLink4,
        y2.otherLink5
      ];

      this.otherLinkIcon2 = ["", "", "", ""];

      for (let i = 0; i < link2.length; i++) {
        for (let j = 0; j < site.length; j++) {
          if (link2[i].indexOf(site[j]) != -1) {
            this.otherLinkIcon2[j] = link2[i];
            break;
          }
        }
      }
    },
    openNewWindow(str) {
      window.open(str);
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
    failCallback() {
      window.location.reload();
    },
    tc(num) {
      return tc(num);
    },
    comma(x) {
      return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }
  },
  computed: {},
  data() {
    return {
      status: {},
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
      totalVideoCountData: [],
      videoPeriodData: [],
      videoPeriodOptions: {
        series: [],
        chart: {
          type: "line",
          zoom: {
            enabled: false
          },
          toolbar: {
            show: false
          }
        },
        dataLabels: {
          enabled: true
        },
        stroke: {
          width: 3,
          curve: "smooth"
        },
        title: {
          align: "center"
        },
        grid: {
          row: {
            colors: ["#f3f3f3", "transparent"],
            opacity: 0.5
          }
        },
        xaxis: {
          categories: ["25주전"]
        }
      },
      subscriberPeriodData: [],
      subscriberPeriodOptions: {
        series: [],
        chart: {
          type: "line",
          zoom: {
            enabled: false
          },
          toolbar: {
            show: false
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          width: 3,
          curve: "smooth"
        },
        title: {
          align: "center"
        },
        grid: {
          row: {
            colors: ["#f3f3f3", "transparent"],
            opacity: 0.5
          }
        },
        xaxis: {
          type: "datetime",
          categories: []
        },
        tooltip: {
          y: {
            formatter: function(x) {
              if (x == null) {
                return 0;
              }
              return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
            }
          }
        },
        yaxis: {
          labels: {
            show: true,
            formatter: value => {
              return tc(value);
            }
          }
        }
      },
      totalViewPeriodData: [],
      totalViewPeriodOptions: {
        series: [],
        chart: {
          type: "line",
          zoom: {
            enabled: false
          },
          toolbar: {
            show: false
          }
        },
        dataLabels: {
          enabled: false
        },
        tooltip: {
          y: {
            formatter: function(x) {
              if (x == null) {
                return 0;
              }
              return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
            }
          }
        },
        stroke: {
          width: 3,
          curve: "smooth"
        },
        title: {
          align: "center"
        },
        grid: {
          row: {
            colors: ["#f3f3f3", "transparent"],
            opacity: 0.5
          }
        },
        xaxis: {
          type: "datetime",
          categories: []
        },
        yaxis: {
          labels: {
            show: true,
            formatter: value => {
              return tc(value);
            }
          }
        }
      },
      otherLinkIcon1: [],
      otherLinkIcon2: [],
      totalViewDiffData: [],
      totalViewDiffOptions: {
        series: [],
        chart: {
          type: "line",
          zoom: {
            enabled: false
          },
          toolbar: {
            show: false
          }
        },
        dataLabels: {
          enabled: false
        },
        tooltip: {
          y: {
            formatter: function(x) {
              return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
            }
          }
        },
        stroke: {
          width: 3,
          curve: "smooth"
        },
        title: {
          align: "center"
        },
        grid: {
          row: {
            colors: ["#f3f3f3", "transparent"],
            opacity: 0.5
          }
        },
        xaxis: {
          type: "datetime",
          categories: []
        },
        yaxis: {
          labels: {
            show: true,
            formatter: value => {
              return tc(value);
            }
          }
        }
      },
      istwoyoutuber: true
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
