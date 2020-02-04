<template>
  <div>
    <h1>comparePage</h1>
    <!-- header -->

    <v-container>
      <v-row>
        <!-- youtuber1 -->
        <v-col cols="5">
          <v-row>
            <v-col cols="6" class="pa-3">
              <v-img class="circle" :src="youtuber1.thumbnails" flat :aspect-ratio="1/1" />
            </v-col>
            <v-col cols="6" class="pb-0">
              <p class="font-weight-black thin display-1 ma-0">{{youtuber1.channelName}}</p>
            </v-col>
          </v-row>
        </v-col>

        <v-col cols="2" align-center>
          <v-divider vertical></v-divider>
        </v-col>

        <!-- youtuber2 -->
        <v-col cols="5">
          <v-row>
            <v-col cols="6" class="pa-3">
              <v-img class="circle" :src="youtuber2.thumbnails" flat :aspect-ratio="1/1" />
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import http from "../vuex/http-common";
import axios from "axios";

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
    const youtuber1Search = new Promise((resolve, reject) => {
      http
        .get("/youtuber/" + this.youtubers[0].yno)
        .then(response => {
          resolve(response.data.data);
        })
        .catch(err => {
          reject(err);
        });
    });

    const youtuber2Search = new Promise((resolve, reject) => {
      http
        .get("/youtuber/" + this.youtubers[1].yno)
        .then(response => {
          resolve(response.data.data);
        })
        .catch(err => {
          reject(err);
        });
    });

    Promise.all([youtuber1Search, youtuber2Search]).then(
      axios.spread((...responses) => {
        this.youtuber1 = responses[0];
        this.youtuber2 = responses[1];

        console.log(this.youtuber1);
        console.log(this.youtuber2);
      })
    );
  },
  methods: {},
  computed: {},
  data() {
    return {
      youtubers: [],
      youtuber1: {},
      youtuber2: {}
    };
  }
};
</script>

<style scoped>
.circle {
  border-radius: 50%;
}
</style>
