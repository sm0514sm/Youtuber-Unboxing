<template>
  <!-- Footer -->
  <mdb-footer color="unique-color-dark" class="page-footer font-small pt-0">
    <div style="backgroundColor: #6351ce">
      <mdb-container class="text-center"></mdb-container>
    </div>
    <mdb-container
      class="mt-5 mb-4 text-center text-md-left"
      style="margin-left:auto; margin-right:auto"
    >
      <div>
        <mdb-row class="mt-3" style="margin-left:auto; margin-right:auto">
          <mdb-col md="5" lg="5" xl="3" class="mb-4">
            <h6 class="text-uppercase font-weight-bold">
              <strong>TEAM LOGO</strong>
            </h6>
            <hr
              class="deep-purple accent-2 mb-4 mt-0 d-inline-block mx-auto"
              style="width: 60px"
            />
            <v-img :src="require('@/assets/7.png')" width="100px"></v-img>
          </mdb-col>
          <mdb-col md="4" lg="3" xl="3" class="mb-4">
            <h6 class="text-uppercase font-weight-bold">
              <strong>Company name</strong>
            </h6>
            <hr
              class="deep-purple accent-2 mb-4 mt-0 d-inline-block mx-auto"
              style="width: 60px"
            />
            <h6 class="text-uppercase font-weight-bold">
              <strong>SSAFY First Project</strong>
            </h6>
            <h6>
              <br />
            </h6>
            <h6 class="text-uppercase font-weight-bold">
              <strong>Class 1 Group 8</strong>
            </h6>
            <h6>
              <br />
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
              class="deep-purple accent-2 mb-4 mt-0 d-inline-block mx-auto"
              style="width: 60px"
            />
            <h6 class="text-uppercase font-weight-bold">
              <strong>Seoul, Gangnam-gu</strong>
            </h6>
            <h6 class="text-uppercase font-weight-bold">
              <strong>Yeoksam-dong</strong>
            </h6>
            <h6 class="text-uppercase font-weight-bold">
              <strong>212 Teheran-ro</strong>
            </h6>
            <h6 class="text-uppercase font-weight-bold">
              <strong>8AM - 6PM</strong>
            </h6>
            <h6 class="text-uppercase font-weight-bold">
              <strong>+82) 1588 - 3357</strong>
            </h6>
          </mdb-col>
        </mdb-row>
      </div>
    </mdb-container>
    <div class="footer-copyright text-center py-3">
      <mdb-container fluid>
        &copy; 2020 Copyright:
        <a href="http://localhost:3000">Youtuber Unboxing</a>
        <div v-if="isIdle" class="transparent"></div>
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
          this.$session.destroy();
          console.log(this.$route.path);
          alert("자동 로그아웃 되었습니다");
          this.$router.go("/");
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
