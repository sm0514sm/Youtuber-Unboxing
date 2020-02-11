<template>
  <div>
    <v-card>
      <v-card-title class="justify-center py-6" style="background-color:#cdcdcd ; height : 300px">
        <i class="font-weight-black display-3">MemberPage</i>
      </v-card-title>
    </v-card>
    <v-container name="container" background-color="transparent">
<template>
  <v-card flat>
    <v-card-text>
      <v-container fluid>
        <v-toolbar-title>관심 항목 설정</v-toolbar-title>
        <p>{{ interest }}</p>
        <v-row>
          <v-col cols="12" sm="4" md="4">
            <v-switch
              v-model="interest"
              label="패션"
              color="red"
              value='0'
              hide-details
            ></v-switch>
            <v-switch
              v-model="interest"
              label="화장품/뷰티"
              color="pink"
              value='1'
              hide-details
            ></v-switch>
            <v-switch
              v-model="interest"
              label="디지털/가전"
              color="purple"
              value="2"
              hide-details
            ></v-switch>
          </v-col>
          <v-col cols="12" sm="4" md="4">
            <v-switch
              v-model="interest"
              label="식품"
              color="indigo"
              value="3"
              hide-details
            ></v-switch>
            <v-switch
              v-model="interest"
              label="출산/육아"
              color="blue"
              value="4"
              hide-details
            ></v-switch>
            <v-switch
              v-model="interest"
              label="생활/건강"
              color="cyan"
              value="5"
              hide-details
            ></v-switch>
          </v-col>
          <v-col cols="12" sm="4" md="4">
            <v-switch
              v-model="interest"
              label="공연/레저/문화"
              color="green"
              value="6"
              hide-details
            ></v-switch>
            <v-switch
              v-model="interest"
              label="스포츠/레저"
              color="yellow"
              value="7"
              hide-details
            ></v-switch>
            <v-switch
              v-model="interest"
              label="여행"
              color="orange"
              value="8"
              hide-details
            ></v-switch>
          </v-col>
        </v-row>
        <v-btn class="ma-2" :loading="loading" :disabled="loading" color="info" @click="loader = 'loading'; getRecommend()">
      유튜버 추천 받기
      <template v-slot:loader>
        <span class="custom-loader">
          <v-icon light>cached</v-icon>
        </span>
      </template>
    </v-btn>
      </v-container>
    </v-card-text>
  </v-card>
</template>


<v-divider inset></v-divider>
<template>
  <v-data-table
    :headers="headers"
    :items="fav"
    sort-by="subscriber"
    class="elevation-1"
  >
  
    <template v-slot:top>
      <v-toolbar flat color="white">
        <v-toolbar-title>내 즐겨찾기 목록</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider>
      </v-toolbar>
    </template>
    <template v-slot:item.action="{ item }">
      <v-icon small @click="deleteItem(item)" color="red">
        delete
      </v-icon>
      
    </template>

    <template v-slot:item.thumbnails="{ item }">
                <v-card color="#00000000" flat :to="{ path: 'youtuberPage', query: { yno : item.yno}}">
                  <v-row>
                    <v-col cols="2" class = "px-0">
                      <v-card color="#00000000"   width="50px" flat>
                        <v-responsive :aspect-ratio="1/1">
                          <v-img class="circle" :src="item.thumbnails" flat/>
                        </v-responsive>
                      </v-card>
                    </v-col>
                    <v-col cols="10" class = "px-0">
                      <v-container fill-height>
                        <v-layout align-center>
                          <v-flex xs12 text-xs-center><div class="font-weight-light">{{item.channelName}}</div></v-flex>
                        </v-layout>
                      </v-container>
                    </v-col>
                  </v-row>
                </v-card>
              </template>
  </v-data-table>
</template>
    </v-container>
  </div>
</template>
<script>
import http from "../vuex/http-common";
  export default {
    data: () => ({
      headers: [
        { text: '채널 이름', align:'left', value:'thumbnails', sortable:false},
        { text: '구독자', value: 'subscriber' },
        { text: '시청수', value: 'totalViewCount' },
        { text: '영상수', value: 'totalVideoCount' },
        { text: '등급', value: 'grade' },
        { text: '삭제', value: 'action', sortable: false },
      ],
      headers1: [
        { text: '채널 이름', align:'left', value:'thumbnails', sortable:false},
        { text: '구독자', value: 'subscriber' },
        { text: '시청수', value: 'totalViewCount' },
        { text: '영상수', value: 'totalVideoCount' },
        { text: '등급', value: 'grade' },
      ],
      fav: [],
      user: [],
      interest: ['1','2','4','5'],
      recommend: [],
      loader: null,
      loading: false,
    }),
    watch: {
      loader () {
        const l = this.loader
        this[l] = !this[l]
        setTimeout(() => (this[l] = false), 1000)
        this.loader = null
      },
    },
    created () {
      this.basicInfo()
      this.initialize()
    },
    mounted(){
    },

    methods: {
      getRecommend(){
        console.log("recommed")
        console.log(this.interest)
      },
      basicInfo(){
        http.get("/user/"+this.$session.get('token'))
        .then(response=>{
          this.user=response.data.data
        })
      },
      initialize () {
        http.get("/favorite/user/"+this.$session.get('token'))
        .then(response=>{
          this.fav = response.data.data
        })
      },
      deleteItem (item) {
        const index = this.fav.indexOf(item)
        if(confirm('Are you sure you want to delete this item?')){
          this.fav.splice(index, 1)
          let par = item.yno+"&"+this.$session.get('token')
      let deleteUrl = "/favorite/delete/"+par
      http.delete(deleteUrl)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
        }
      },
      
    },
  }
</script>
<style scoped>
.jb {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.circle{
  border-radius: 50%;
}

 .custom-loader {
    animation: loader 1s infinite;
    display: flex;
  }
  @-moz-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @-webkit-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @-o-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
</style>
