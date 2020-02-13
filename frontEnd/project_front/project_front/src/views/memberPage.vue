<template>
  <div>
    <v-card>
      <v-card-title class="justify-center py-6" style="background-color:#cdcdcd ; height : 300px">
        <i class="font-weight-black display-3">MemberPage</i>
      </v-card-title>
    </v-card>
    <v-container name="container" background-color="transparent">

      <template>
        <v-hover v-slot:default="{ hover }" open-delay="100">
  <v-card
  :elevation="hover ? 7 : 1" 
    class="mx-auto"
    outlined
  >
  
    <v-list-item three-line>
      
      <v-list-item-avatar
        tile
        size="80"
        color="grey"
      ></v-list-item-avatar>
      <v-list-item-content>
        <v-list-item-title class="headline mb-1"><v-chip
      class="ma-2"
      color="indigo"
      text-color="white"
    >
      <v-avatar left>
        <v-icon>mdi-account-circle</v-icon>
      </v-avatar>
      닉네임
    </v-chip>{{user.userName}}</v-list-item-title>
    <div v-if="user.userEmail">
    <v-list-item-title class="headline mb-1"><v-chip
      class="ma-2"
      color="green"
      text-color="white"
    >
      <v-avatar left>
        <v-icon>mdi-email</v-icon>
      </v-avatar>
      이메일
    </v-chip>{{user.userEmail}}</v-list-item-title>
    </div>
      </v-list-item-content>

    </v-list-item>

    <v-card-actions>
      <v-btn color="error" text @click="logout2">Logout</v-btn>
    </v-card-actions>
  </v-card>
  </v-hover>
</template>

<v-divider inset></v-divider>

<template>
  <v-hover v-slot:default="{ hover }" open-delay="100">
  <v-card flat :elevation="hover ? 7 : 1">
    <v-card-text>
      <v-container fluid>

        <v-toolbar-title>관심 항목 설정</v-toolbar-title>
        <template v-if='interest.length>2'>
          <div>
            <span class="red--text">최대 3개 제한</span>
          </div>
          <div>
            <span class="red--text">{{ interest }}</span>
          </div>
        </template>
        <v-row>
          <v-col cols="12" sm="4" md="4">
            <v-switch
              v-model="interest"
              :disabled="check('0')"
              label="패션"
              color="red"
              value='0'
              hide-details
            ></v-switch>
            <v-switch
              v-model="interest"
              :disabled="check('1')"
              label="화장품/뷰티"
              color="pink"
              value='1'
              hide-details
            ></v-switch>
            <v-switch
              v-model="interest"
              :disabled="check('2')"
              label="디지털/가전"
              color="purple"
              value="2"
              hide-details
            ></v-switch>
          </v-col>
          <v-col cols="12" sm="4" md="4">
            <v-switch
              v-model="interest"
              :disabled="check('3')"
              label="식품"
              color="indigo"
              value="3"
              hide-details
            ></v-switch>
            <v-switch
              v-model="interest"
              :disabled="check('4')"
              label="출산/육아"
              color="blue"
              value="4"
              hide-details
            ></v-switch>
            <v-switch
              v-model="interest"
              :disabled="check('5')"
              label="생활/건강"
              color="cyan"
              value="5"
              hide-details
            ></v-switch>
          </v-col>
          <v-col cols="12" sm="4" md="4">
            <v-switch
              v-model="interest"
              :disabled="check('6')"
              label="공연/레저/문화"
              color="green"
              value="6"
              hide-details
            ></v-switch>
            <v-switch
              v-model="interest"
              :disabled="check('7')"
              label="스포츠/레저"
              color="yellow"
              value="7"
              hide-details
            ></v-switch>
            <v-switch
              v-model="interest"
              :disabled="check('8')"
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
  </v-hover>
</template>






<template>
  
  <v-card
    class="mx-auto"
  >
    <v-container fluid>
      <v-toolbar-title>추천 유튜버</v-toolbar-title>
      <v-row>
        <v-col
          v-for="card in recommend"
          :key="card.title"
          :cols="6"
        >
        <v-hover v-slot:default="{ hover }" open-delay="100">
          <v-card
          :elevation="hover ? 9 : 3"
            class="mx-auto"
            height="100%"
            color=""
          >
            <v-list-item>
              <v-list-item-avatar size="100" @click="goTo(card.yno)"><img
                :src="card.thumbnails"
                alt="thumnnail"
              ></v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title class="headline" v-text="card.channelName" @click="goTo(card.yno)"></v-list-item-title>
                <v-list-item-subtitle>개설일 : {{card.publishedDate}}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>

            <v-card-text>
              {{card.channelDescription}}
            </v-card-text>
            
            <v-card-actions >
              <v-btn
                text
                color="deep-purple accent-4"
              >
                Read
              </v-btn>
              <v-btn
                text
                color="deep-purple accent-4"
              >
                Bookmark
              </v-btn>
              <v-spacer></v-spacer>
              <v-btn text icon color="yellow">
                <v-icon v-if="flag" @click="deleteFav(card.yno)" x-large>mdi-star</v-icon>
                <v-icon v-if="!flag" @click="insertFav(card.yno)" x-large>mdi-star-outline</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-hover>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>







<v-divider inset></v-divider>
<template>
  <v-hover v-slot:default="{ hover }" open-delay="100">
    <v-card :elevation="hover ? 7 : 1">
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

    <template v-slot:item.channelName="{item}">
      <div @click="goTo(item.yno)">{{item.channelName}}</div>
    </template>

    <template v-slot:item.thumbnail="{ item }">
      <v-avatar @click="goTo(item.yno)">
      <img
        :src="item.thumbnails"
        alt="John"
      >
    </v-avatar>
    </template>
  </v-data-table>
    </v-card>
  </v-hover>
</template>
    </v-container>
  </div>
</template>


<script>
import http from "../vuex/http-common";
  export default {
    data: () => ({
      flag: false,
      headers: [
        {text: '', value:'thumbnail', sortable:false},
        { text: '채널 이름', value:'channelName', sortable:false},
        { text: '구독자', value: 'subscriber' },
        { text: '시청수', value: 'totalViewCount' },
        { text: '영상수', value: 'totalVideoCount' },
        { text: '등급', value: 'grade' },
        { text: '삭제', value: 'action', sortable: false },
      ],
      fav: [],
      user: [],
      interest: [ 1,3,
    4,
    ],
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
      http.get("interest/search/"+this.$session.get("token"))
      .then(res=>{
        var temp =[]
        this.interest = res.data.data
        this.interest.forEach(el=>temp.push(el+""))
        this.interest=temp
        this.getRecommend()
      })
    },

    methods: {
      logout2(){
        let a
            let result = new Promise((resolve, reject)=>{
                http
                .get("/logout/" + this.$session.get('token'))
                .then(response => { 
                    a=response.data.data.responseCode
                    if(a=='200'){
                        this.$session.destroy()
                        console.log(this.$route.query)
                        if(this.$route.path=='/memberPage'){
                            this.$router.push('/')
                        }
                        window.location.reload()
                    }
                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
            })
            console.log(result)
            this.$session.destroy()
            if(this.$route.path=='/memberPage'){
                this.$router.push('/')
            }
            window.location.reload()

      },
    insertFav(yno){
      console.log("insert")
      console.log(this.$session.get('token'))
      http.get('/favorite/insert/'+yno+"&"+this.$session.get('token'))
      .then(function (response) {
        console.log(response);
        this.flag=true
        this.initialize()
      })
      .catch(function (error) {
        console.log(error);
      });
    },
    deleteFav(yno){
      console.log("delete")
      console.log(this.$session.get('token'))
      let par = yno+"&"+this.$session.get('token')
      let deleteUrl = "/favorite/delete/"+par
      http.delete(deleteUrl)
      .then(function (response) {
        console.log(response);
        this.flag=false
        this.initialize()
      })
      .catch(function (error) {
        console.log(error);
      });
    },
      goTo(yno){
        console.log(yno)
        let link = 'youtuberPage?yno='+yno
        this.$router.push(link)
      },
      check(a){
        if(this.interest.length>2 && !(this.interest.includes(a))){
          return true
        }else return false
      },
      getRecommend(){
        console.log("recommed")
        console.log(this.interest)
        var link = this.$session.get("token")+"&"+this.interest
        console.log(link)
        http.get("/interest/search/recommend/"+link)
        .then(res=>{
          this.recommend = res.data.data
        })
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
        console.log(item)
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
