<template>
  <!-- Footer -->
  <mdb-footer color="#222222" class="page-footer font-small pt-0">
    <!-- <hr
      class="pink mb-4 mt-0 d-inline-block mx-auto"
      style="width: -webkit-fill-available; margin-left:20px;margin-right:20px"
    />-->
    <hr
      style="border: 1px solid lightgray; margin-left:35px; margin-right:35px; margin-bottom: 30px"
    />
    <mdb-container class="text-center text-md-left" style="margin-left:auto; margin-right:auto">
      <div>
        <mdb-row style="margin-left:auto; margin-right:auto">
          <mdb-col col="3">
            <h5 class="text-uppercase">
              <strong>COMPANY</strong>
            </h5>
            <hr style="width: 60px; border: 0.5px solid #222222;" />
            <v-img :src="require('@/assets/footer.png')" width="100px"></v-img>
          </mdb-col>
          <mdb-col col="5">
            <h5 class="text-uppercase font-weight-800">
              <strong>PROJECT NAME</strong>
            </h5>
            <hr style="width: 60px; border: 0.5px solid #222222;" />
            <h6>SSAFY FIRST PROJECT</h6>
            <h6 class="text-uppercase">Class 1 Group 8</h6>
            <h6 class="text-uppercase">Web / Mobile Application</h6>
          </mdb-col>
          <mdb-col col="4">
            <h5 class="text-uppercase">
              <strong>Contact</strong>
            </h5>
            <hr style="width: 60px; border: 0.5px solid #222222;" />
            <h6 class="text-uppercase">Seoul, Gangnam-gu, Yeoksam-dong</h6>
            <h6 class="text-uppercase">212 Teheran-ro, 9AM - 6PM</h6>
            <h6 class="text-uppercase">+82) 1588 - 3357</h6>
            <h6 class="text-uppercase">+82) 1588 - 3357</h6>
          </mdb-col>
        </mdb-row>
      </div>
    </mdb-container>
    <div v-if="isIdle" class="transparent"></div>
    <div class="footer-copyright text-center pb-2 mb-5">
      <mdb-container fluid>
        &copy; 2020 Copyright:
        <a href="http://15.165.77.1:3000">Youtuber Unboxing</a>
      </mdb-container>
    </div>
  </mdb-footer>
  <!-- Footer -->
</template>

<script>
import { mdbFooter, mdbContainer, mdbRow, mdbCol } from "mdbvue";
import http from "../vuex/http-common";
export default {
  computed: {
    isIdle() {
      if (this.$session.get("token")) {
        if (this.$store.state.idleVue.isIdle) {
          http.get("/logout/" + this.$session.get("token"));
          alert("자동 로그아웃 되었습니다");
          this.$session.destroy();
          console.log(this.$route.path);
        }
      }
      return this.$store.state.idleVue.isIdle;
    }
  },
  name: "FooterPage",
  components: {
    mdbFooter,
    mdbContainer,
    mdbRow,
    mdbCol
  }
};
</script>
