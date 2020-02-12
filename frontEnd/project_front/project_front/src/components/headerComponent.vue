<template>
  <v-app-bar
    id="app_bar_tt"
    :color="headerColor"
    fixed
    elevate-on-scroll
    scroll-threshold="500"
    v-scroll="onScroll"
  >
    <v-img
      :src="require('@/assets/logo.png')"
      class
      contain
      height="48"
      width="48"
      max-width="48"
      @click="gotoHome"
    />

    <v-spacer />
    <!-- 유튜버 추가 -->
    <input-component></input-component>

    <!-- 검색 -->
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
      style="max-width: 300px; "
      solo-inverted
      flat
    >
      <template v-slot:no-data>
        <v-list-item>
          <v-list-item-title>검색 결과가 없습니다.</v-list-item-title>
        </v-list-item>
      </template>

      <template v-slot:item="{ item }">
        <v-list-item-avatar color="red" class="headline font-weight-light white--text">
          <img :src="item.thumbnails" alt="John" />
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title v-text="item.channelName"></v-list-item-title>
          <v-list-item-subtitle>{{item.subscriber}}</v-list-item-subtitle>
        </v-list-item-content>
      </template>
    </v-autocomplete>

    <!-- 카카오로그인 -->
    <v-img
      v-if="!loginStatus"
      :src="require('@/assets/kakao.png')"
      class
      contain
      height="100"
      width="100"
      max-width="100"
      @click="login()"
    />
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-if="loginStatus" v-slot:activator="{ on }">
        <v-btn class="ma-2" color="indigo" large outlined dark v-on="on">LOGOUT</v-btn>
        <v-btn class="ma-2" color="indigo" large outlined dark @click="gotoMember()">MY INFO</v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">LogoutModal</span>
        </v-card-title>
        <v-card-text>
          <v-container>정말로 로그아웃 하겠습니까?</v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false">No</v-btn>
          <v-btn color="blue darken-1" text @click="logout()">Yes</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-app-bar>
</template>


<script>
import inputComponent from "./inputComponent";
import { mapGetters } from "vuex";
import http from "../vuex/http-common";
// import axios from "axios";
export default {
  components: {
    inputComponent
  },
  computed: {
    ...mapGetters(["links"])
  },

  mounted() {
    console.log("loginStatus:" + this.loginStatus);
    console.log(this.$session);
    if (!this.$session.exists()) {
      this.loginStatus = false;
      console.log("no session");
    }
    console.log(this.$route.query);
    var token = this.$route.query.access_Token;
    if (token != undefined) {
      this.$session.start();
      this.$session.set("token", token);
      this.loginStatus = true;
      console.log("token:" + this.$session.get("token"));
      this.$router.push("/");
    }
  },
  methods: {
    gotoMember() {
      this.$router.push("/memberPage");
    },
    login() {
      window.location.href =
        "https://accounts.kakao.com/login?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fclient_id%3Dcaca7722fcbd20626b2343a0f5bf4083%26redirect_uri%3Dhttp%3A%2F%2F15.165.77.1%3A8080%2FSpringBootNew%2Flogin%26response_type%3Dcode";
    },
    logout() {
      let a;
      let result = new Promise((resolve, reject) => {
        http
          .get("/logout/" + this.$session.get("token"))
          .then(response => {
            a = response.data.data.responseCode;
            if (a == "200") {
              this.$session.destroy();
              console.log(this.$route.query);
              if (this.$route.path == "/memberPage") {
                this.$router.push("/");
              }
              window.location.reload();
            }
            resolve(response);
          })
          .catch(err => {
            reject(err);
          });
      });
      console.log(result);
      this.$session.destroy();
      if (this.$route.path == "/memberPage") {
        this.$router.push("/");
      }
      window.location.reload();
    },

    isDisabled() {
      return true;
    },
    gotoHome(e) {
      e.stopPropagation();
      if (this.$route.path === "/") {
        this.$vuetify.goTo(0);
        //window.location.reload()
        return;
      }
      this.$router.push("/", () => {});
      return;
    },
    search: function() {
      console.log(document.getElementById("keyword").value)
      this.$router.push(
        { path: "/searchPage", query: { word: document.getElementById("keyword").value } },
        () => {}
      );
      document.getElementById("keyword").vaule = ""
    },
    onScroll() {
      var scroll = window.pageYOffset;
      var value = "#cdcdcd";
      var position = 250;
      if (scroll >= position) {
        value += "ff";
      } else {
        var tmp = Math.round((scroll / position) * parseInt("FF", 16)).toString(
          16
        );
        if (tmp.length == 1) {
          value += "0" + tmp;
        } else {
          value += tmp;
        }
      }

      this.headerColor = value;
    }
  },
  data() {
    return {
      loginStatus: true,
      searchWord: "",
      dialog: false,
      headerColor: "transparent",
      searchItems: [],
      inputKeyword: null
    };
  },
  creted() {
    this.headerColor = "#00000000";

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
        })
        .catch(err => {
          console.log(err);
        })
    }
  },
};
</script>

<style scoped>
#header {
  background-color: #999999;
  position: absolute;
}

.v-toolbar__content,
.v-toolbar__extension {
  background-color: blue;
  color: blue;
}

.app_bar_tt {
  background-color: blue;
}

.disable-events {
  pointer-events: none;
}
</style>