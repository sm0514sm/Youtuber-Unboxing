<template>
    <!-- vuetify를 참고하여 작성하기
                      https://vuetifyjs.com/ko/components/api-explorer
                      -->
    <div>
     <video 
        class="bgvideo" 
        src="@/assets/iu2.webm" 
        alt="main-picture" 
        width="100%" 
        autoplay="" 
        loop="true" 
        muted=""
        style="margin: 0 auto; padding: 0;"
    ></video>
    <!-- <image-preloader
    :src="require('@/assets/coolcat.png')">
    </image-preloader> -->

    <div style="position: absolute; top: 10%; left: 30%; font-size: 56px; font-weight: 400; color: white; text-shadow: -1px 0 rgba(0, 0, 0, 0.1), 0 1px  rgba(0, 0, 0, 0.1), 1px 0 rgba(0, 0, 0, 0.1), 0 -1px  rgba(0, 0, 0, 0.1);">
        {{typo}}
        <div style="display: inline; color: rgba(255, 255, 255, 0.8)">{{cursor}}</div>
    </div>

    <div style="position: absolute; top: 14.5%; left: 37%; width: 300px;">
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
      >
        <template v-slot:no-data>
          <v-list-item>
            <v-list-item-title>검색 결과가 없습니다.</v-list-item-title>
          </v-list-item>
        </template>

        <template v-slot:item="{ item }">
          <v-list-item-avatar color="red" class="headline font-weight-light white--text">
            <img :src="item.thumbnails" alt="John" />
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title v-text="item.channelName"></v-list-item-title>
            <v-list-item-subtitle>구독자 : {{tc(item.subscriber)}}</v-list-item-subtitle>
          </v-list-item-content>
        </template>
      </v-autocomplete>
      <br>
    </div>
    <div class="allCategory">
            <div class="categorySet">
                <!-- <v-btn block :aspect-ratio="1/1" @click="onCategoryButtonClicked(0)" class="categorySet"> -->
                   <v-icon @click="onCategoryButtonClicked(0)" class="material-icons">mdi-widgets-outline</v-icon>
                <!-- </v-btn> -->
                <div class="categoryName">전체</div>
            </div>
            <div class="categorySet">
                <v-icon @click="onCategoryButtonClicked(1)" class="material-icons">mdi-gamepad-variant</v-icon>
                <div class="categoryName">게임</div>
            </div>
            <div class="categorySet">
                <v-icon @click="onCategoryButtonClicked(2)" class="material-icons">mdi-television-classic</v-icon>
                <div class="categoryName">엔터</div>
            </div>
            <div class="categorySet">
                <v-icon @click="onCategoryButtonClicked(3)" class="material-icons">mdi-palette</v-icon>
                <div class="categoryName">노하우</div>
            </div>
            <div class="categorySet">
                <v-icon @click="onCategoryButtonClicked(4)" class="material-icons">mdi-weight-lifter</v-icon>
                <div class="categoryName">운동</div>
            </div>
            <div class="categorySet">
                <v-icon @click="onCategoryButtonClicked(5)" class="material-icons">mdi-food</v-icon>
                <div class="categoryName">음식</div>
            </div>
            <div class="categorySet">
                <v-icon @click="onCategoryButtonClicked(6)" class="material-icons">mdi-baby-face-outline</v-icon>
                <div class="categoryName">키즈</div>
            </div>
            <div class="categorySet">
                <v-icon @click="onCategoryButtonClicked(7)" class="material-icons">mdi-dog</v-icon>
                <div class="categoryName">동물</div>
            </div>
            <div class="categorySet">
                <v-icon @click="onCategoryButtonClicked(8)" class="material-icons">mdi-camera-outline</v-icon>
                <div class="categoryName">일상</div>
            </div>
            <div class="categorySet">
                <v-icon @click="onCategoryButtonClicked(9)" class="material-icons">mdi-cellphone-iphone</v-icon>
                <div class="categoryName">기술</div>
            </div>
      </div>
       
        <!-- <v-img :src="require('@/assets/giphy2.gif')" width="100%"></v-img> -->

        <div style="margin: 0; padding: 0; background-color: antiquewhite; height: 30px;" />
        <br><br>

        <div style="display: flex; width: 100%;">
            <div style="display: inline-block; margin: 0 auto;" width="45%">
                <h1 style="margin-top: 15%; font-weight: bold;">강력한 검색 기능</h1>
                <h3>
                    원하는 유튜버를 검색해 볼 수 있습니다.<br>만약 내가 찾는 유튜버가 없다면?<br>자유롭게 추가하세요<br>
                </h3>
                <input-component></input-component>
            </div>
        
            <div style="display: inline-block; margin: 0 auto;" width="45%;">
                <v-img :src="require('@/assets/main1.gif')" width="500px"></v-img>
            </div>
        </div>

        <br><br>
        <hr>
        <br><br>

        <div style="display: flex; width: 100%;">
            <div style="display: inline-block; margin: 0 auto;" width="45%;">
                <v-img :src="require('@/assets/main2.gif')" width="500px"></v-img>
            </div>
            <div style="display: inline-block; margin: 0 auto;" width="45%">
                <h1 style="margin-top: 15%; font-weight: bold;">완벽한 비교하기 기능</h1>
                <h3>
                    번거롭게 하나하나 비교할 필요 없이<br>한 화면에서 두 유튜버를 비교할 수 <br>있습니다.
                </h3>
            </div>
        </div>

        <br><br>
        <hr>
        <br><br>

        <div style="display: flex; width: 100%;">
            <div style="display: inline-block; margin: 0 auto;" width="45%">
                <h1 style="margin-top: 15%; font-weight: bold;">간편한 즐겨찾기 기능</h1>
                <h3>
                    마음에 드는 유튜버가 있다면<br>클릭 한 번으로 추가하고<br>언제든지 모아보세요
                </h3>
            </div>
        
            <div style="display: inline-block; margin: 0 auto;" width="45%;">
                <v-img :src="require('@/assets/7.png')" width="300px"></v-img>
            </div>
        </div>

        <br><br>
        <hr>
        <br><br>

        <div style="display: flex; width: 100%;">
            <div style="display: inline-block; margin: 0 auto;" width="45%;">
                <v-img :src="require('@/assets/7.png')" width="300px"></v-img>
            </div>
             <div style="display: inline-block; margin: 0 auto;" width="45%">
                <h1 style="margin-top: 15%; font-weight: bold;">완벽한 유튜버 추천 기능</h1>
                <h3>
                    나와 관심항목이 같은 사람들이<br>즐겨찾는 유튜버를 추천해 드립니다<br>바로 확인해 보세요
                </h3>
            </div>
        </div>
        
        <br><br>
<!-- 
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
        </v-container> -->
        
        
        <!-- <v-card>
            <v-img :src="require('@/assets/coolcat.png')" class="py-6 lighten-5">
                <i class="font-weight-black display-4 jb mb-5 pm-5">Youtube Analysis</i>
            </v-img>
        </v-card> -->
    
        <!-- <banner /> -->
    
        <!-- <v-container transition="slide-y-transition">
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
        </v-container> -->
    </div>
</template>

<script>
// import banner from "../components/banner";
import inputComponent from "../components/inputComponent";
import http from "../vuex/http-common";
import {
    mapGetters
} from 'vuex';
import tc from "thousands-counter";



export default {
    components: {
        inputComponent
        // banner 
    },
    name: "mainPage",
    methods: {
        search: function() {
        console.log(document.getElementById("keyword").value);
        this.$router.push({
            path: "/searchPage",
            query: { word: document.getElementById("keyword").value }
            }, () => {});
        document.getElementById("keyword").vaule = "";
        },
        onCategoryButtonClicked(i) {
            localStorage.setItem('currentCategory',i)
            this.$router.push("/categoryPage");
        },
        startCursor() {
            let toggleCursor = false;
            setInterval(() => {
                const cur = toggleCursor ? ' |' : ' ';
                this.cursor = cur;
                toggleCursor = !toggleCursor;
            }, 200);
        },
        startTypo() {
            const lifeCopy = 'Youtuber Unboxing... ';
            // const lifeCopy = '샤이니 이상해 나 배고파 배고파... ';
            let isRight = true;
            let idx = 9;
            setInterval(() => {
                const len = lifeCopy.length;

                isRight ? idx++ : idx--;
                if(idx >= len) isRight = false;
                else if(idx === 8) isRight = true;

                this.typo = lifeCopy.slice(0, idx);
            }, 300);
        },
        tc(num){
            return tc(num)
        }

    },
    computed: {
        ...mapGetters(['categories']),
        ...mapGetters(['youtubersPerCategory']),
    },
    data() {
        return {
            tmp: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            layout: [2, 2, 1, 2, 2, 3, 3, 3, 3, 3, 3],
            typo: 'Youtuber Unboxing...',
            cursor: '|',
            searchWord: "",
            searchItems: [],
            inputKeyword: null
        };
    },
    mounted() {
        this.startTypo();
        this.startCursor();
    },
    watch: {
    inputKeyword() {
      // Items have already been loaded
      if (this.searchItems.length > 10) return;
      // Lazily load input items
      http
        .get("/youtuber/all")
        .then(response => {
          this.searchItems = response.data.data;
        })
        .catch(err => {
          console.log(err);
        });
    }
    }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Do+Hyeon|Nanum+Gothic|Noto+Sans+KR&display=swap');
.jb {
    text-align: center;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate( -50%, -50%);
    color: black;
    background-color: #95b3e8a9;
    margin-bottom: 50px;
}
.rounded-card{   
    border-radius:20%;
    box-shadow: none;
}
.categoryName {
    font-family: PT sans;
    color: blacks;
    text-align: center;
}
/* .des_title {
    font-size: 3.125rem;
    margin-bottom: 0.5rem;
} */
.bgvideo {
    height: 100%;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}
div {
    font-family: 'Noto Sans KR', sans-serif;
}
/* .material-icons.md-18 { font-size: 18px; } */
/* .material-icons.md-24 { font-size: 24px; } */

/* .material-icons.md-48 { font-size: 48px; } */

/* Rules for using icons as black on a light background. */
/* .material-icons.md-dark { } */
    
/* .material-icons.md-dark.md-inactive { color: rgba(0, 0, 0, 0.26); } */

/* Rules for using icons as white on a dark background. */
/* .material-icons.md-light { color: rgba(255, 255, 255, 1); } */
/* .material-icons.md-light.md-inactive { color: rgba(255, 255, 255, 0.3); } */
.allCategory {
    position: absolute; 
    top: 20%; 
    left: 50%; 
    transform:translateX(-50%); 
    width: 780px; 
    background-color: #e3dada66;
}
.material-icons { 
    font-size: 52px;
    color: rgba(0, 0, 0, 0.54); 
    background-color: white; 
    border-radius: 20%; 
    /* margin: 0px 3px;  */
    padding: 7px;
}
.categorySet {
    text-align: center;
    float: left;
    width: 66px;
    margin: 6px;
}
.categoryName {
    position: static;
    /* margin: 0px 6px; */
    padding: 0px 2px;
    width: 66px;
    color: white;
}
</style>
