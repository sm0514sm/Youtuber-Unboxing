<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on }">
        <v-btn color="primary" dark v-on="on" @click="init"
          >유튜버 추가하기</v-btn
        >
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">유튜버 추가하기</span>
        </v-card-title>
        <v-card-text>
          <!--inputPage -->
          <v-container v-if="nowPage == 'inputPage'">
            <v-row>
              <v-col cols="12">원하는 유튜버의 주소를 복사해주세요.</v-col>
              <v-col cols="12">
                <v-img :src="require('@/assets/youtuberinsert.png')"></v-img>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  label="주소"
                  v-model="address"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
          <!--loadingPage -->
          <v-container v-else-if="nowPage == 'loadingPage'">
            <v-row>
              <v-col cols="12">데이터 요청중입니다 ... [ 남은 예상 시간 : {{ Math.round(44 - value/2) }}초 ]</v-col>
            </v-row>
            <v-row>
              <v-spacer></v-spacer>
              <v-col>
                <v-progress-circular
                  :rotate="360"
                  :size="100"
                  :width="15"
                  :value="value"
                  color="teal"
                  >{{ value }}</v-progress-circular
                >
              </v-col>
              <v-spacer></v-spacer>
            </v-row>
          </v-container>
          <!--completePage -->
          <v-container v-else-if="nowPage == 'completePage'">
            <v-row>
              <v-col cols="12">
                <p
                  style="text-align: center;color: red;font-size: 20px;"
                  class="pa-0"
                >
                  {{ completeTitle }}
                </p>
              </v-col>
              <v-col cols="12">
                <p style="text-align: center;" class="pa-0">
                  {{ completeSmallTitle }}
                </p>
              </v-col>
            </v-row>
            <v-row>
              <v-spacer></v-spacer>
              <v-col>
                <v-btn
                  large
                  v-if="youtuberPage"
                  color="blue darken-1"
                  text
                  @click="gotoYoutuberPage"
                  >해당 유튜버의 페이지로 이동하기</v-btn
                >
              </v-col>
              <v-spacer></v-spacer>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false"
            >Close</v-btn
          >
          <v-btn
            v-if="nowPage == 'inputPage'"
            color="blue darken-1"
            text
            @click="onSendButton"
            >SEND</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import Constant from "../vuex/Constant.js";
export default {
  components: {},
  name: "inputComponent",
  methods: {
    onSendButton: function() {
      this.nowPage = "loadingPage";
      this.$store.dispatch(Constant.INSERT_YOUTUBUER, {
        address: this.address,
        callback: this.processDispatch
      });
    },
    processDispatch: function(code, yno) {
      console.log("processDispatch" + code + " " + code + " " + yno);
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
          this.completeSmallTitle =
            "구독자 10만명이하인 유튜버는 insert를 지원 하지 않습니다.";
        } else {
          // 서버문제로 지원 안 함.
          this.completeSmallTitle = "서버 에러";
        }
      }
      this.nowPage = "completePage";
      console.log(code);
    },
    init: function() {
      this.nowPage = "inputPage";
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
    }
  },
  computed: {
    value() {
      return this.$store.state.value;
    },
    myyno() {
      return this.$store.state.yno;
    },
    tempValue(){
        return this.$store.state.tempValue;
    }
},
  data() {
    return {
      dialog: false,
      address: "",
      nowPage: "inputPage",
      completeTitle: "",
      completeSmallTitle: "",
      youtuberPage: false,
      youtuberYno: "",
      interval: {},
      lastValue: 0
    };
  },
  beforeDestroy() {
    clearInterval(this.interval);
  },
  mounted() {
    this.interval1 = setInterval(() => {
        if (this.nowPage == "loadingPage") {
            if(this.myyno == null || this.myyno <= 0){
                this.$store.dispatch(Constant.GET_YNO_FROM_URL, {
                    url: this.address,
                })
            }
            else{
                clearInterval(this.interval1)
                return;
            }
        }
    }, 2000);
    this.interval2 = setInterval(() => {
        if(this.myyno != null && this.myyno > 0){
            clearInterval(this.interval1)
            this.$store.dispatch(Constant.GET_STATUS_FROM_YNO, {
                yno: this.myyno,
            })
        }
        if(this.value >= 100){
            this.value = 100;
            clearInterval(this.interval2)
            return;
        }
    }, 500);
    this.interval3 = setInterval(() => {
        if(this.value >= 100){
            clearInterval(this.interval3)
            return;
        }
        if(this.myyno != null && this.myyno > 0 && this.tempValue + 40 > this.value){
            this.$store.state.value = this.value + Math.round((Math.random() * 2.5));
        }
    }, 1000);
  }
};
</script>

<style scoped></style>
