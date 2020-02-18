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
          <mdb-col md="5" lg="5" xl="3" class="mb-4">
            <h6 class="text-uppercase font-weight-bold">
              <strong>COMPANY</strong>
            </h6>
            <hr
              class="mb-4 mt-0 d-inline-block mx-auto"
              style="width: 60px; border: 0.5px solid #222222;"
            />
            <v-img :src="require('@/assets/footer.png')" width="100px"></v-img>
          </mdb-col>
          <mdb-col md="4" lg="3" xl="3" class="mb-4">
            <h6 class="text-uppercase font-weight-bold">
              <strong>PROJECT NAME</strong>
            </h6>
            <hr
              class="mb-4 mt-0 d-inline-block mx-auto"
              style="width: 60px; border: 0.5px solid #222222;"
            />
            <h6 class="text-uppercase font-weight-bold">
              <strong>SSAFY First Project</strong>
            </h6>
            <h6 class="text-uppercase font-weight-bold">
              <strong>Class 1 Group 8</strong>
            </h6>
            <h6 class="text-uppercase font-weight-bold">
              <strong>Web / Mobile Application</strong>
            </h6>
          </mdb-col>
          <mdb-col md="4" lg="3" xl="4" class="mb-4">
            <h6 class="text-uppercase font-weight-bold">
              <strong>Contact</strong>
            </h6>
            <hr
              class="mb-4 mt-0 d-inline-block mx-auto"
              style="width: 60px; border: 0.5px solid #222222;"
            />
            <h6 class="text-uppercase font-weight-bold">
              <strong>Seoul, Gangnam-gu, Yeoksam-dong</strong>
            </h6>
            <h6 class="text-uppercase font-weight-bold">
              <strong>212 Teheran-ro, 9AM - 6PM</strong>
            </h6>
            <h6 class="text-uppercase font-weight-bold">
              <strong>+82) 1588 - 3357</strong>
            </h6>
          </mdb-col>
        </mdb-row>
      </div>
    </mdb-container>
    <div v-if="isIdle" class="transparent"></div>
    <div class="footer-copyright text-center pb-5">
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
