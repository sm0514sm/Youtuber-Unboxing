<template>
  <div>
    <v-card
        v-for="(item,i) in searchedyoutuber.slice(0,10)"
        :key="i"
        class="my-3 pa-0"
        outlined
        flat
        @click="gotoYoutuberPage(item.yno)"
      >
        <v-container fluid class="pa-1">
          <v-row class="px-5">
            <!-- thumbnail -->
            <v-col cols="2" class="pa-3">
              <v-layout row>
                <v-flex justify-center>
                  <v-img class="circle" :src="item.thumbnails" flat :aspect-ratio="1/1" />
                </v-flex>
              </v-layout>
            </v-col>

            <!-- 기본정보 -->
            <v-col cols="8" class="px-7">
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

            <v-col cols="2" class="pa-3">
              <v-layout row>
                <v-flex justify-center>
                  <v-btn
                    fab
                    :color="setGradeColor(item.grade)"
                    style="width: 100%;height: 0;padding-bottom: 50%; padding-top: 50%;"
                    
                  >
                    <p
                      style="text-align: center;position: absolute;top: 50%;left: 50%;transform: translate(-50%, -50%);color: white;font-size: 120px;"
                    >{{setGrade(item.grade)}}</p>
                  </v-btn>
                </v-flex>
              </v-layout>
            </v-col>
          </v-row>
        </v-container>
      </v-card>
  </div>
</template>


<script>
import http from "../vuex/http-common";
export default {
  name: "TestPage",
  components: {},
  data: () => ({
    searchItems: [],
    inputKeyword: null,
  }),
  created() {
http
        .get("/youtuber/all")
        .then(response => {
          console.log(response.data.data);
          this.searchItems = response.data.data;
        })
        .catch(err => {
          console.log(err);
        })
  },

  watch: {
    
    inputKeyword() {
      // Items have already been loaded
      if (this.searchItems.length > 0) return;


      // Lazily load input items
      http
        .get("/youtuber/all")
        .then(response => {
          console.log(response.data.data);
          this.searchItems = response.data.data;
        })
        .catch(err => {
          console.log(err);
        })
    }
  },
  methods: {
    search: function() {
      console.log("*************"+document.getElementById("keyword").value)
      this.$router.push(
        { path: "/searchPage", query: { word: document.getElementById("keyword").value } },
        () => {}
      );
    },
  }
};
</script>

<style scoped>
</style>