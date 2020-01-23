<template>
  <!-- vuetify를 참고하여 작성하기
  https://vuetifyjs.com/ko/components/api-explorer
  -->
  <v-container>
    <h1>categoryPage</h1>

    <v-btn v-for="(c,i) in categories" :key="i"  @click="onCategoryButtonClicked(c.nameEng)" >{{c.nameKor}}</v-btn>

    <hr>

    <keep-alive>
      <category-component :selectedCategory=category></category-component>
    </keep-alive>
    
  </v-container>
</template>

<script>
import categoryComponent from "../components/categoryComponent";
import {
    mapGetters
}from 'vuex'

export default {
  components: {categoryComponent},
  name: "categoryPage",

  created(){
  },
  methods: {
    onCategoryButtonClicked(str){
      this.category = str;
    },
  },
  computed: {
    ...mapGetters(['categories'])
  },
  data() {
    return { 
      category : (this.$route.params.cate === undefined?"game":this.$route.params.cate)
      };
  },
  
};
</script>

<style scoped></style>
