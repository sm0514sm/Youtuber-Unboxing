<template>
  <!-- vuetify를 참고하여 작성하기
                      https://vuetifyjs.com/ko/components/api-explorer
  -->
  <div>
    <video
      :src="require('@/assets/bg' + bgNum + '.mp4')"
      class="bgvideo"
      alt="main-picture"
      width="100%"
      autoplay
      loop="true"
      muted
      style="margin: 0 auto; padding: 0;"
    ></video>

    <div class="websiteName">
      {{ typo }}
      <div style="display: inline; color: rgba(255, 255, 255, 0.8)">{{ cursor }}</div>
    </div>

    <div class="searchForm">
      <v-autocomplete
        :items="searchItems"
        :search-input.sync="inputKeyword"
        hide-details
        item-text="channelName"
        item-value="channelName"
        @keyup.enter="search"
        ref="keyword"
        id="keyword"
        label="유튜버를 검색해보세요"
        background-color="rgba(255, 255, 255, 0.95)"
        height="50px"
      >
        <template v-slot:no-data>
          <v-list-item>
            <v-list-item-title>검색 결과가 없습니다.</v-list-item-title>
          </v-list-item>
        </template>

        <template v-slot:item="{ item }">
          <div v-if="item.yno == -1" class="ma-0 pa-0"></div>
          <v-list-item-avatar
            v-if="item.yno != -1"
            color="red"
            class="headline font-weight-light white--text"
            @click="gotoYoutuberPage(item.yno)"
          >
            <img :src="item.thumbnails" alt="John" />
          </v-list-item-avatar>
          <v-list-item-content
            v-if="item.yno != -1"
            style="width: 100px"
            @click="gotoYoutuberPage(item.yno)"
          >
            <v-list-item-title v-text="item.channelName"></v-list-item-title>
            <v-list-item-subtitle>구독자 : {{ tc(item.subscriber) }}</v-list-item-subtitle>
          </v-list-item-content>
        </template>
      </v-autocomplete>
      <br />
    </div>
    <div class="allCategory">
      <div class="categorySet" @click="onCategoryButtonClicked(0)" style="cursor:pointer">
        <v-icon class="material-icons" color="red">mdi-widgets-outline</v-icon>
        <div class="categoryName">전체</div>
      </div>

      <div
        class="categorySet"
        v-for="(item,index) in categories"
        :key="index+1"
        @click="onCategoryButtonClicked(index+1)"
        style="cursor:pointer"
      >
        <v-icon class="material-icons" :color="item.iconColor">{{item.icon}}</v-icon>
        <div class="categoryName">{{item.iconName}}</div>
      </div>
    </div>
  </div>
</template>

<script>
import http from "../vuex/http-common";
import { mapGetters } from "vuex";
import tc from "thousands-counter";

export default {
  components: {},
  name: "mainPage",
  methods: {
    search: function() {
      console.log(document.getElementById("keyword").value);
      this.$router.push(
        {
          path: "/searchPage",
          query: { word: document.getElementById("keyword").value }
        },
        () => {}
      );
      document.getElementById("keyword").vaule = "";
    },
    onCategoryButtonClicked(i) {
      localStorage.setItem("currentCategory", i);
      this.$router.push("/categoryPage");
    },
    startCursor() {
      let toggleCursor = false;
      setInterval(() => {
        const cur = toggleCursor ? " |" : " ";
        this.cursor = cur;
        toggleCursor = !toggleCursor;
      }, 200);
    },
    startTypo() {
      const lifeCopy = "Youtuber Unboxing... ";
      let isRight = true;
      let idx = 9;
      setInterval(() => {
        const len = lifeCopy.length;

        isRight ? idx++ : idx--;
        if (idx >= len) isRight = false;
        else if (idx === 8) isRight = true;

        this.typo = lifeCopy.slice(0, idx);
      }, 300);
    },
    tc(num) {
      return tc(num);
    },
    gotoYoutuberPage(yno) {
      this.$router.push({ path: "youtuberPage", query: { yno: yno } });
    }
  },
  mounted() {
    this.$vuetify.goTo(0);
    document.getElementById("keyword").parentElement.style.marginLeft = "12px";
    document.getElementById("keyword").parentElement.style.marginTop = "3px";
  },
  computed: {
    ...mapGetters(["categories"]),
    ...mapGetters(["youtubersPerCategory"])
  },
  data() {
    return {
      tmp: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
      layout: [2, 2, 1, 2, 2, 3, 3, 3, 3, 3, 3],
      typo: "Youtuber Unboxing...",
      cursor: "|",
      searchWord: "",
      searchItems: [],
      inputKeyword: null
    };
  },
  created() {
    this.startTypo();
    this.startCursor();
    this.bgNum = Math.floor(Math.random() * 13 + 1);
  },
  watch: {
    inputKeyword() {
      // Items have already been loaded
      if (this.searchItems.length > 10) return;
      // Lazily load input items
      http
        .get("/youtuber/all")
        .then(response => {
          this.searchItems = response.data.data;
          var tmp = { yno: -1, channelName: [] };
          for (let index = 0; index < response.data.data.length; index++) {
            tmp["channelName"] += response.data.data[index].channelName;
          }
          this.searchItems.push(tmp);
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Do+Hyeon|Nanum+Gothic|Noto+Sans+KR&display=swap");
.rounded-card {
  border-radius: 20%;
  box-shadow: none;
}
.categoryName {
  font-family: "Noto Sans KR", sans-serif;
  color: blacks;
  text-align: center;
}
.bgvideo {
  height: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
div {
  font-family: "Noto Sans KR", sans-serif;
}
.allCategory {
  position: absolute;
  top: 55%;
  left: 50%;
  transform: translateX(-50%);
  width: 780px;
  background-color: rgba(0, 0, 0, 0.2);
  border-radius: 20px;
  /* background-color: #e3dada66; */
}
.material-icons {
  font-size: 52px;
  color: rgba(0, 0, 0, 0.54);
  background-color: white;
  border-radius: 20%;
  /* margin: 0px 3px;  */
  padding: 7px;
}
.categorySet {
  text-align: center;
  float: left;
  width: 66px;
  margin: 6px;
}
.categoryName {
  position: static;
  /* margin: 0px 6px; */
  padding: 0px 2px;
  width: 66px;
  color: white;
  text-shadow: rgb(0, 0, 0) 0px 0px 10px;
}
.websiteName {
  position: absolute;
  top: 27%;
  left: 32%;
  font-size: 56px;
  font-weight: 400;
  color: white;
  text-shadow: rgb(0, 0, 0) 0px 0px 7px;
}
.searchForm {
  position: absolute;
  top: 37%;
  left: 50%;
  transform: translateX(-50%);
  width: 400px;
}
.searchForm div {
  border-radius: 5px 5px 0px 0px;
}
.v-label {
  padding-left: 50px;
}
</style>
