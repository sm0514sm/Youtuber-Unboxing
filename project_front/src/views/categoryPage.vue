<template>
  <div>
    <v-card>
      <v-card-title class="justify-center py-6" style="background-color:#F29661 ; height : 300px">
        <i class="font-weight-black" style="font-size : 100px">CATEGORY</i>
      </v-card-title>
    </v-card>
    <v-container name="container" background-color="transparent">
      <v-tabs :value="currentCategory" background-color="transparent" grow>
        <v-tab key="0" @click="onCategoryButtonClicked(0)">ALL</v-tab>
        <v-tab
          v-for="(item,index) in categories"
          :key="index+1"
          @click="onCategoryButtonClicked(index+1)"
        >{{ item. nameEng}}</v-tab>
      </v-tabs>

      <v-tabs-items :value="currentCategory">
        <v-tab-item key="0">
          <v-card flat class="pa-3" color="#FAFAFA">
            <v-card-title class="pa-0" style="background-color : white">
              <v-spacer></v-spacer>
              <v-spacer></v-spacer>
              <v-spacer></v-spacer>

              <v-text-field
                v-model="search"
                append-icon="search"
                label="원하는 유튜버를 검색해보세요"
                single-line
                hide-details
                class="mr-5 mb-5"
              ></v-text-field>
            </v-card-title>
            <v-data-table :headers="headers" :items="youtubersPerCategory" :search="search">
              <template v-slot:item.insertCompare="{ item }">
                <v-btn
                  @click="onClikcedinsertCompare(item.yno,item.channelName)"
                  text
                  color="green"
                >
                  <v-icon dark>input</v-icon>비교담기
                </v-btn>
              </template>

              <!-- 썸네일과 channelName -->
              <template v-slot:item.channelName="{ item }">
                <v-card
                  color="#00000000"
                  flat
                  :to="{ path: 'youtuberPage', query: { yno : item.yno}}"
                >
                  <v-row class="ml-3">
                    <v-col cols="2" class>
                      <v-card color="#00000000" width="50px" flat class="ml-5">
                        <v-responsive :aspect-ratio="1/1">
                          <v-img class="circle" :src="item.thumbnails" flat />
                        </v-responsive>
                      </v-card>
                    </v-col>
                    <v-col cols="10" class>
                      <v-container fill-height>
                        <v-layout align-center>
                          <v-flex xs12 text-xs-center>
                            <div class="font-weight-light">{{item.channelName}}</div>
                          </v-flex>
                        </v-layout>
                      </v-container>
                    </v-col>
                  </v-row>
                </v-card>
              </template>
              <template v-slot:item.subscriber="{ item }">{{tc(item.subscriber)}}</template>
              <template v-slot:item.grade="{ item }">{{setGrade(item.grade)}}</template>
            </v-data-table>
          </v-card>
        </v-tab-item>

        <v-tab-item v-for="(item,index) in categories" :key="index+1">
          <v-card flat class="pa-3" color="#FAFAFA">
            <v-card-title class="pa-0" style="background-color : white">
              <v-spacer></v-spacer>
              <v-spacer></v-spacer>
              <v-spacer></v-spacer>

              <v-text-field
                v-model="search"
                append-icon="search"
                label="원하는 유튜버를 검색해보세요"
                single-line
                hide-details
                class="mr-5 mb-5"
              ></v-text-field>
            </v-card-title>
            <v-data-table
              flat
              :headers="headers"
              :items="youtubersPerCategory"
              class="elevation-1"
              :search="search"
            >
              <template v-slot:item.insertCompare="{ item }">
                <v-btn
                  @click="onClikcedinsertCompare(item.yno,item.channelName)"
                  text
                  color="green"
                >
                  <v-icon dark>input</v-icon>비교담기
                </v-btn>
              </template>

              <!-- 썸네일 -->
              <template v-slot:item.channelName="{ item }">
                <v-card
                  color="#00000000"
                  flat
                  :to="{ path: 'youtuberPage', query: { yno : item.yno}}"
                >
                  <v-row>
                    <v-col cols="2" class="px-0">
                      <v-card color="#00000000" width="50px" flat>
                        <v-responsive :aspect-ratio="1/1">
                          <v-img class="circle" :src="item.thumbnails" flat />
                        </v-responsive>
                      </v-card>
                    </v-col>
                    <v-col cols="10" class="px-0">
                      <v-container fill-height>
                        <v-layout align-center>
                          <v-flex xs12 text-xs-center>
                            <div class="font-weight-light">{{item.channelName}}</div>
                          </v-flex>
                        </v-layout>
                      </v-container>
                    </v-col>
                  </v-row>
                </v-card>
              </template>

              <template v-slot:item.subscriber="{ item }">{{tc(item.subscriber)}}</template>

              <template v-slot:item.grade="{ item }">{{setGrade(item.grade)}}</template>

            </v-data-table>
          </v-card>
        </v-tab-item>
      </v-tabs-items>
    </v-container>
  </div>
</template>


<script>
import { mapGetters } from "vuex";
import Constant from "../vuex/Constant";
import EventBus from "../components/eventBus";
import tc from "thousands-counter";

export default {
  components: {},
  name: "categoryPage",

  methods: {
    onCategoryButtonClicked(index) {
      localStorage.setItem("currentCategory", index);
      console.log("*************" + index);
      if (index == 0) {
        this.$store.dispatch(Constant.GET_ALLYOUTUBER, {
          failCallback: this.failCallback
        });
      } else {
        this.$store.dispatch(Constant.GET_YOUTUBERS_PER_CATEGORY, {
          failCallback: this.failCallback,
          category: this.findCano()
        });
      }
    },
    findCano: function() {
      return this.categories[localStorage.getItem("currentCategory") - 1].cano;
    },
    onClikcedinsertCompare: function(yno, channelName) {
      EventBus.$emit("insertYoutuber", yno, channelName);
    },
    tc(num) {
      return tc(num);
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
    }
  },
  mounted() {
    this.$vuetify.goTo(0);
    console.log("*taetae********" + localStorage.getItem("currentCategory"));
    if (localStorage.getItem("currentCategory") == 0) {
      this.$store.dispatch(Constant.GET_ALLYOUTUBER, {
        failCallback: this.failCallback
      });
      return;
    }
    this.$store.dispatch(Constant.GET_YOUTUBERS_PER_CATEGORY, {
      failCallback: this.failCallback,
      category: this.findCano()
    });
  },
  created() {},

  computed: {
    ...mapGetters(["categories"]),
    ...mapGetters(["youtubersPerCategory"]),
    currentCategory() {
      return Number(localStorage.getItem("currentCategory"));
    }
  },
  watch: {},
  data() {
    return {
      headers: [
        { text: "", value: "", sortable: false, width: "%" },
        { text: "", value: "channelName", sortable: false, width: "25%" },
        { text: "구독자수", value: "subscriber" },
        { text: "영향력", value: "influence" },
        { text: "활동력", value: "activity" },
        { text: "조회수력", value: "viewCountTrend" },
        { text: "구독자력", value: "subscriberCountTrend" },
        { text: "호감도", value: "charm" },
        { text: "등급", value: "grade" },
        { text: "", value: "insertCompare", sortable: false }
      ],
      search: ""
    };
  }
};
</script>

<style scoped>
.jb {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.circle {
  border-radius: 50%;
}
</style>
