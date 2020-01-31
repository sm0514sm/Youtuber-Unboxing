<template>
  <!-- vuetify를 참고하여 작성하기
  https://vuetifyjs.com/ko/components/api-explorer
  -->
  <v-container>
    <h1> searchPage </h1>
    "{{$route.query.word}}" 를 검색한 결과
    <h1> Youtuber </h1>
    <hr>

    <v-container wrap style="background : gray">
      <v-card v-for="(item,i) in searchyoutuber" :key=i class="ma-5" >
        <v-container>
          <v-row> 
          <v-col justify="space-between">
            <v-col width>
              <v-card
                height="200"
                width="200"
                :img="item.thumbnails"
                :to= "{ path: 'youtuberPage', query: { yno : item.yno}}"
              />
            </v-col>
          </v-col>

          <v-col>
            <h1> {{item.channelName}} </h1>
            {{item.channelDescription}} <br>
            {{item.regDate}}
          </v-col>
          </v-row>
        </v-container>
      </v-card>
    </v-container>
    
  </v-container>
  
  
</template>

<script>
import {
    mapGetters
}from 'vuex'
import Constant from"../vuex/Constant";


export default {
  components: {},
  name: "categoryPage",

  
  methods: {
    
    
  },
  created(){
        console.log(this.$route.query)
        this.$store.dispatch(Constant.SEARCH_YOUTUBER, {
          searchWord : this.$route.query.word
        })
  },
  computed: {
    ...mapGetters(['searchyoutuber']),
  },
  watch: {
    '$route' (to,from) {
        if (to.path === '/searchPage') {
          if(to.query.word != from.query.word){
            this.$store.dispatch(Constant.SEARCH_YOUTUBER, {
            searchWord : to.query.word
        })
          }
        }
      }
  }
};
</script>

<style scoped></style>
