<template>
  <!-- vuetify를 참고하여 작성하기
                      https://vuetifyjs.com/ko/components/api-explorer
  -->

  <div>
    <image-preloader :src="require('@/assets/coolcat.png')"></image-preloader>

    <v-card>
      <v-img :src="require('@/assets/coolcat.png')">
        <v-container fluid>
          <v-layout column>
            <v-flex xs12>
              <div class="resultContainer">
                <v-layout align-center justify-center row fill-height column style="margin-top : 100px">
                <!-- 이미지 -->
                  <v-img :src="require('@/assets/3.png')"></v-img>
                <!-- 검색 -->
                  <v-autocomplete
                    :items="searchItems"
                    :search-input.sync="inputKeyword"
                    hide-details
                    item-text="channelName"
                    item-value="channelName"
                    @keyup.enter="search"
                    ref="keyword"
                    id="keyword"
                    label="유튜버를 검색해보세요"
                    style="max-width: 300px; "
                    solo-inverted
                    flat
                    class="mt-3"
                  >
                    <template v-slot:no-data>
                      <v-list-item>
                        <v-list-item-title>검색 결과가 없습니다.</v-list-item-title>
                      </v-list-item>
                    </template>

                    <template v-slot:item="{ item }">
                      <v-list-item-avatar
                        color="red"
                        class="headline font-weight-light white--text"
                      >
                        <img :src="item.thumbnails" alt="John" />
                      </v-list-item-avatar>
                      <v-list-item-content>
                        <v-list-item-title v-text="item.channelName"></v-list-item-title>
                        <v-list-item-subtitle>구독자 : {{tc(item.subscriber)}}</v-list-item-subtitle>
                      </v-list-item-content>
                    </template>
                  </v-autocomplete>
                </v-layout>
              </div>
            </v-flex>
          </v-layout>
        </v-container>
      </v-img>
    </v-card>

    <!-- <banner />
    
        <v-container transition="slide-y-transition">
            <v-layout wrap class="pa-12 ma-10">
                <v-flex v-for="(category,i) in categories" :key=i xs6 md4 class="pa-8" background-color="none">
                    <v-responsive :aspect-ratio="1/1">
                        <v-btn block :aspect-ratio="1/1" @click="onCategoryButtonClicked(i)" height="100%" width="50px" class="rounded-card">
                            <v-img :src="require('@/assets/' + i + '.png')" class="rounded-card pa-5">
                                
                            </v-img>
                        </v-btn>
                    </v-responsive>
                    <h1 class="categoryName"> {{category.nameEng}} </h1>
                </v-flex>
            </v-layout>
    </v-container>-->
  </div>
</template>

<script>
// import banner from "../components/banner";
// import inputComponent from "../components/inputComponent";
// import {
//     mapGetters
// } from 'vuex'

// export default {
//     components: {
//         // inputComponent,
//         banner
//     },
//     name: "mainPage",
//     methods: {
//         onCategoryButtonClicked(i) {
//             localStorage.setItem('currentCategory',i)
//             this.$router.push("/categoryPage");
//         },
//     },
//     computed: {
//         ...mapGetters(['categories']),
//         ...mapGetters(['youtubersPerCategory']),
//     },
//     data() {
//         return {
//             tmp: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
//             layout: [2, 2, 1, 2, 2, 3, 3, 3, 3, 3, 3]
//         };
//     },
// };
</script>

<style scoped>
.jb {
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: black;
  /* background-color: #95b3e8a9; */
  margin-bottom: 50px;
}
.rounded-card {
  border-radius: 20%;
  box-shadow: none;
}
.categoryName {
  font-family: PT sans;
  color: blacks;
  text-align: center;
}
/* #maindiv {
  height: 100vh;
} */
</style>