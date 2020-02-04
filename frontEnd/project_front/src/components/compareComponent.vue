<template>
  <v-menu
    open-on-hover
    top
    offset-y
    :close-on-content-click="false"
    :nudge-width="200"
    :nudge-top="20"
    :close-delay="300"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-btn v-bind="attrs" v-on="on" fab fixed bottom right></v-btn>
    </template>

    <v-list>
      <v-list-item>
        <v-card>
          <h1>비교하고 싶은 유튜버</h1>
          <v-row v-for="(item,index) in youtubers" :key="index">
            <v-col cols="7">{{item.channelName}}</v-col>
            <v-spacer></v-spacer>
            <v-col>
              <v-btn @click="deleteYoutber(item.yno)">삭제</v-btn>
            </v-col>
          </v-row>
        </v-card>
      </v-list-item>
      <v-list-item>
        <v-btn @click="gotoComparePage">비교하기</v-btn>
      </v-list-item>
      <v-list-item>
        <v-card>최근 본 유튜버</v-card>
        <a target="_blank" href="https://www.naver.com">Policies</a>
      </v-list-item>
    </v-list>
  </v-menu>
</template>

<script>
import EventBus from "./eventBus";


export default {
  computed: {},
  watch: {},
  methods: {
    updateyoutubers: function() {
      console.log("updateyoutubers");
      var output = localStorage.getItem("compareYoutuber");
      var arr = JSON.parse(output);
      this.youtubers = arr;
      return this.youtubers;
    },
    deleteYoutber: function(yno) {
      console.log(yno);
      var output = localStorage.getItem("compareYoutuber");
      var arr = JSON.parse(output);
      const idx = arr.findIndex(function(item) {
        return item.yno === yno;
      });
      if (idx > -1) arr.splice(idx, 1);
      localStorage.setItem("compareYoutuber", JSON.stringify(arr));
      this.updateyoutubers();
    },
    gotoComparePage : function() {
      console.log("gotoComparePage")
      this.$router.push("/comparePage");
    }
    
  },
  created() {
    EventBus.$on("changeCompareYoutuber", this.updateyoutubers);
    var output = localStorage.getItem("compareYoutuber");
    var arr = JSON.parse(output);
    this.youtubers = arr;
  },
  data: () => ({
    youtubers: []
  })
};
</script>

