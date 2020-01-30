<template>
  <!-- vuetify를 참고하여 작성하기
  https://vuetifyjs.com/ko/components/api-explorer
  -->
  <div>
    <v-card>
      <v-card-title class="justify-center py-6" style="background-color:#cdcdcd ; height : 300px">
        <i class="font-weight-black display-3" color="red">YOUTUBERPAGE</i>
      </v-card-title>
    </v-card>
    <v-container>
      <v-card flat>
        <v-img :src="youtuber.bannerImageLink" class="py-6 lighten-5">
          <!-- <i class="font-weight-black display-4 jb">YOUTUBER</i> -->
        </v-img>
      </v-card>
      {{this.$route.query.yno}}
      <v-divider></v-divider>
      {{youtuber.yno}}
      <br />
      {{youtuber.channelName}}
      <br />
      {{youtuber.youtuberName}}
      <br />
      {{youtuber.channelDescription}}
      <br />
      {{youtuber.namuwiki}}
      <br />
      {{youtuber.instagram}}
      <br />
      {{youtuber.facebook}}
      <br />
      {{youtuber.thumbnails}}
      <br />
      {{youtuber.publishedDate}}
      <br />
      {{youtuber.subscriber}}
      <br />
    </v-container>
  </div>
</template>

<script>
import {
  // mapState,
  mapGetters
} from "vuex";
import Constant from "../vuex/Constant";

export default {
  components: {},
  name: "youtuberPage",
  created() {
    console.log(this.$route.query);
    this.$store.dispatch(Constant.GET_YOUTUBER, {
      yno: this.$route.query.yno
    });
    console.log(this.$store.state.youtuber.yno);
  },
  methods: {},
  computed: {
    ...mapGetters({
      youtuber: "youtuber"
    })
  },
  data() {
    return {};
  }
};
</script>

<style scoped></style>
