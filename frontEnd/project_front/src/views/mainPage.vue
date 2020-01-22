<template>
  <!-- vuetify를 참고하여 작성하기
  https://vuetifyjs.com/ko/components/api-explorer
  -->
  <div>
    <banner />
  <v-container >
    <v-layout wrap>
      <v-flex 
        v-for="(category,i) in categories"
        :key = i
        xs12
        md4
        class="pa-3"
        >
      <v-btn 
        block class="ma-5" 
        :to="{ name: 'categoryPage', params: { cate: category.nameEng }}">
      <h1 > {{category.nameEng}} </h1>
      </v-btn>
      </v-flex>

    </v-layout>
    
    <h1 v-for=" a in  tmp" :key="a">
      back에 no 3으로 testID값 얻기 위해 GET요청 보내기
    </h1>

  </v-container>
  </div>
</template>

<script>
import banner from "../components/banner";
import {
    mapGetters
}from 'vuex'


export default {
  components: { banner },
  name: "mainPage",
  methods: { },
  computed: {
    ...mapGetters(['categories'])
  },
  data() {
    return {
      tmp : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
      layout: [2, 2, 1, 2, 2, 3, 3, 3, 3, 3, 3]
    };
  }
};
</script>

<style scoped>


</style>
