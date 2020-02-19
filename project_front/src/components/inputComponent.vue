<template>
  <v-col cols="3" align="center">
    <v-dialog v-model="dialog" persistent max-width="550px">
      <template v-slot:activator="{ on }">
        <!-- main -->
        <v-btn
          v-if="position == 'main'"
          style="font-size: 15px; font-family: 'Noto Sans KR', 'sans-serif;'"
          v-on="on"
          :loading="loading"
          :disabled="loading"
          color="red"
          @click="init"
          dark
          class="pl-2 pr-3 mt-2"
        >
          <v-icon class="mr-2">mdi-youtube</v-icon>유튜버 추가하기
        </v-btn>
        <!-- header -->
        <v-btn
          v-else-if="position == 'header'"
          style="font-size: 20px; text-shadow: 0 0 2px #000;"
          v-on="on"
          :loading="loading"
          :disabled="loading"
          color="white"
          text
          @click="init"
        >ADD YOUTUBER</v-btn>
        <!-- search -->
        <v-btn
          v-if="position == 'search'"
          style="font-size: 20px;"
          v-on="on"
          :loading="loading"
          :disabled="loading"
          color="blue"
          @click="init"
          dark
          rounded
        >
          <v-icon large>mdi-account-circle</v-icon>유튜브 추가하기
        </v-btn>
      </template>
      <v-card class="pa-5">
        <v-card-title align="center" class="pa-0">
          <v-row>
            <v-col class="mx-1">
              <p class="display-2 font-weight-black">
                <v-icon color="red" size="40">mdi-youtube</v-icon>유튜버
                추가하기
              </p>
            </v-col>
          </v-row>
        </v-card-title>
        <v-divider class="ma-0"></v-divider>
        <v-card-text class="pb-0">
          <!--inputPage -->
          <v-container v-if="nowPage == 'inputPage'">
            <v-row>
              <v-col cols="12">
                원하는 유튜버의 채널 주소를 복사해주세요!
                <br />
                <a target="_blank" href="https://www.youtube.com/">
                  <v-icon>mdi-youtube</v-icon>유튜브 페이지 이동
                </a>
              </v-col>
              <v-col cols="12">
                <v-img :src="require('@/assets/youtuberinsert.png')"></v-img>
              </v-col>
              <v-col cols="12">
                <v-text-field label="주소" v-model="address" required append-icon="language"></v-text-field>
              </v-col>
            </v-row>
          </v-container>
          <!--loadingPage -->
          <v-container v-else-if="nowPage == 'loadingPage'">
            <v-row>
              <v-col cols="12">
                데이터 요청중입니다 ... [ 남은 예상 시간 :
                {{ Math.round(35 - value / 2.86) }}초 ]
              </v-col>
            </v-row>
            <v-row>
              <v-spacer></v-spacer>
              <v-col>
                <v-progress-circular
                  :rotate="360"
                  :size="200"
                  :width="30"
                  :value="value"
                  color="teal"
                >
                  <h2>
                    <b>{{ Math.round(value)==0?"Loading...":Math.round(value) }}</b>
                  </h2>
                </v-progress-circular>
              </v-col>
              <v-spacer></v-spacer>
            </v-row>
          </v-container>
          <!--completePage -->
          <v-container v-else-if="nowPage == 'completePage'">
            <v-row>
              <!-- 추가 완료했을 때 -->
              <v-col v-if="pageCode === 0" cols="12">
                <animation-css :animation-type="AnimationType.TADA" v-model="animationFlag">
                  <p style="text-align: center;color: #2196F3 ;font-size: 20px;" class="pa-0">
                    <v-icon color="blue" x-large>mdi-human-handsup</v-icon>
                    {{ completeTitle }}
                    <v-icon color="blue" x-large>mdi-human-handsup</v-icon>
                  </p>
                </animation-css>
              </v-col>
              <!-- 그외 에러 났을 때 -->
              <v-col v-else cols="12">
                <animation-css :animation-type="AnimationType.HEADSHAKE" v-model="animationFlag">
                  <p style="text-align: center;color: red ;font-size: 15px;" class="pa-0">
                    <v-icon color="red" x-large>mdi-alert</v-icon>
                    {{ completeTitle }}
                    <v-icon color="red" x-large>mdi-alert</v-icon>
                  </p>
                </animation-css>
              </v-col>
              <v-col cols="12">
                <p style="text-align: center;" class="pa-0">{{ completeSmallTitle }}</p>
              </v-col>
            </v-row>
            <v-row>
              <v-spacer></v-spacer>
              <v-col>
                <v-btn
                  large
                  v-if="pageCode == 0 || pageCode == 1"
                  color="blue darken-1"
                  text
                  @click="gotoYoutuberPage"
                >해당 유튜버의 페이지로 이동하기</v-btn>
              </v-col>
              <v-spacer></v-spacer>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="onCloseButton">닫기</v-btn>
          <v-btn v-if="nowPage == 'inputPage'" color="blue darken-1" text @click="onSendButton">추가하기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <div class="text-center">
      <v-snackbar
        class="ml-3"
        v-model="snackbar"
        :absolute="true"
        color="blue-grey lighten-3"
        :timeout="100000"
      >
        <v-progress-linear
          v-if="snackProgress"
          color="blue-grey"
          :buffer-value="0"
          :value="value"
          stream
        />
        <v-icon large dark @click="snackbar = false">clear</v-icon>
      </v-snackbar>
    </div>
  </v-col>
</template>
<script>
import Constant from "../vuex/Constant.js";
import { AnimationCss, AnimationCssType } from "vue-animation";
export default {
  components: {
    [AnimationCss.name]: AnimationCss
  },
  props: ["position"],
  name: "inputComponent",
  methods: {
    onSendButton: function() {
      console.log("interval 함수들 실행");
      this.$store.state.value = 0;
      this.nowPage = "loadingPage";
      this.$store.dispatch(Constant.INSERT_YOUTUBUER, {
        address: this.address,
        callback: this.processDispatch
      });
      this.intervalSetting();
      this.snackbar = true;
      this.snackProgress = true;
      this.loader = "loading";
    },
    onCloseButton: function() {
      this.dialog = false;
      // clearInterval(this.getYnoInterval);
      // clearInterval(this.getValueInterval);
      // clearInterval(this.addValueInterval);
      // this.address = "";
    },
    processDispatch: function(code, yno) {
      console.log("processDispatch" + code + " " + code + " " + yno);
      this.pageCode = code;
      if (code == 1) {
        // 원래 있던 유튜버가 보여질 때
        this.completeTitle = "추가하려는 유튜버가 이미 있습니다!";
        this.completeSmallTitle = "";
        this.youtuberPage = true;
        this.youtuberYno = yno;
      } else if (code == 0) {
        // 추가가 완료 됐을 때
        this.completeTitle = "유튜버를 추가했습니다!";
        this.completeSmallTitle = "";
        this.youtuberPage = true;
        this.youtuberYno = yno;
      } else {
        //오류 찾기
        this.completeTitle = "유튜버를 추가하는 도중 오류가 발생했습니다.";
        this.youtuberPage = false;
        if (code == -1) {
          // URL이 올바르지 않을 때
          this.completeSmallTitle = "입력한 URL이 올바르지 않습니다.";
        } else if (code == -3) {
          // 너무 인기 없는 유튜버라 지원 안함.
          this.completeTitle = "구독자가 적은 유튜버는 지원하지 않습니다!";
          this.completeSmallTitle =
            "구독자 10만명이하인 유튜버는 [유튜브추가]를 지원 하지 않습니다.";
        } else {
          // 서버문제로 지원 안 함.
          this.completeSmallTitle = "서버 에러";
        }
      }
      this.snackbar = false;
      this.loader = null;
      this.loading = false;
      clearInterval(this.getYnoInterval);
      clearInterval(this.getValueInterval);
      clearInterval(this.addValueInterval);
      this.nowPage = "completePage";
      this.$store.state.yno = 0;
      this.snackProgress = false;
      console.log("snackbar : ", this.snackbar);
    },
    init: function() {
      this.nowPage = "inputPage";
      this.animationFlag = true;
      console.log(this.nowPage);
    },
    gotoYoutuberPage: function() {
      this.dialog = false;
      this.$vuetify.goTo(0);
      this.$router.push({
        path: "/youtuberPage",
        query: {
          yno: this.youtuberYno
        }
      });
    },
    intervalSetting: function() {
      this.getYnoInterval = setInterval(() => {
        // console.log('myyno : ', this.myyno)
        // console.log('1. getYnoInterval 실행')
        if (this.nowPage == "loadingPage") {
          if (this.myyno == null || this.myyno <= 0) {
            this.$store.dispatch(Constant.GET_YNO_FROM_URL, {
              url: this.address
            });
          } else {
            clearInterval(this.getYnoInterval);
            return;
          }
        }
        if (this.myyno > 0) {
          clearInterval(this.getYnoInterval);
        }
      }, 2000);
      this.getValueInterval = setInterval(() => {
        // console.log('2. getValueInterval 실행')
        if (this.myyno != null && this.myyno > 0) {
          clearInterval(this.interval1);
          this.$store.dispatch(Constant.GET_STATUS_FROM_YNO, {
            yno: this.myyno
          });
        }
        if (this.value >= 100) {
          this.value = 100;
          clearInterval(this.getValueInterval);
          return;
        }
      }, 350);
      this.addValueInterval = setInterval(() => {
        // console.log('3. addValueInterval 실행')
        if (this.value >= 100) {
          clearInterval(this.addValueInterval);
          return;
        }
        if (
          this.myyno != null &&
          this.myyno > 0 &&
          this.tempValue + 60 > this.value
        ) {
          if (this.value < 65 && this.value > 0) {
            this.$store.state.value = this.value + 1;
          } else if (this.value < 83 && this.value > 64) {
            this.$store.state.value = this.value + 0.8;
          } else if (this.value < 90 && this.value > 82) {
            this.$store.state.value = this.value + 0.15;
          }
          // this.$store.state.value =
          //   this.value + Math.round(Math.random() * 3.5);
        }
      }, 240);
    },
    test: function() {
      console.log("before" + this.snackbar);
      this.snackbar = true;
      console.log("After" + this.snackbar);
    }
  },
  computed: {
    value() {
      return this.$store.state.value;
    },
    myyno() {
      return this.$store.state.yno;
    },
    tempValue() {
      return this.$store.state.tempValue;
    }
  },
  data() {
    return {
      dialog: false,
      address: "",
      nowPage: "insertPage",
      completeTitle: "",
      completeSmallTitle: "",
      youtuberPage: false,
      youtuberYno: "",
      interval: {},
      lastValue: 0,
      getYnoInterval: "",
      getValueInterval: "",
      addValueInterval: "",
      pageCode: 0,
      AnimationType: AnimationCssType,
      animationFlag: true,
      snackbar: false,
      snackProgress: false,
      y: "top",
      mode: "",
      loader: null,
      loading: false,
      ffalse: false
    };
  },
  beforeDestroy() {
    clearInterval(this.interval);
  },
  mounted() {
    this.intervalSetting();
    clearInterval(this.getYnoInterval);
    clearInterval(this.getValueInterval);
    clearInterval(this.addValueInterval);
  },
  watch: {
    loader() {
      const l = this.loader;
      this[l] = !this[l];
      this.loader = null;
    }
  }
};
</script>
<style scoped>
.v-snack--bottom {
  bottom: -650px;
}
</style>
