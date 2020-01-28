<template>
  <!-- vuetify를 참고하여 작성하기
  https://vuetifyjs.com/ko/components/api-explorer
  -->
  <v-container>
    <h1>youtuberPage</h1>

    {{this.$route.query.yno}}
    <hr>
    {{youtuber.yno}} <br>
    {{youtuber.channelName}}<br>
    {{youtuber.youtuberName}}<br>
    {{youtuber.channelDescription}}<br>
    {{youtuber.namuwiki}}<br>
    {{youtuber.instagram}}<br>
    {{youtuber.facebook}}<br>
    {{youtuber.thumbnails}}<br>
    {{youtuber.publishedDate}}<br>
    {{youtuber.subscriber}}<br>

    
  </v-container>
</template>

<script>
import {
    // mapState,
    mapGetters
}from 'vuex'
import Constant from"../vuex/Constant";

export default {
  components: {
  },
  name: "youtuberPage",
  created(){
    console.log(this.$route.query);
    this.$store.dispatch(Constant.GET_YOUTUBER, {
          yno : this.$route.query.yno
        });
    console.log(this.$store.state.youtuber.yno);
  },
  methods: {
  },
  computed: {
    ...mapGetters({
      youtuber : 'youtuber'}
    ),
  },
  data() {
    return { 
      };
  },
  
};
</script>

<style scoped></style>
