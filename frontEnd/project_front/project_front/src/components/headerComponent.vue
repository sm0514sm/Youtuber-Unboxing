<template>
    <v-app-bar id="app_bar_tt" :color="headerColor" fixed elevate-on-scroll scroll-threshold="500" v-scroll="onScroll">
        <v-img :src="require('@/assets/logo.png')" class="" contain height="48" width="48" max-width="48" @click="gotoHome" />

        <v-spacer />
        <v-text-field class="ma-2" append-icon="mdi-magnify" flat hide-details solo-inverted style="max-width: 300px; " @keyup.enter="search" v-model="searchWord" :key="$route.fullPath" />



        
            <v-dialog v-model="dialog" persistent max-width="600px">
                <template v-slot:activator="{ on }">
                        <v-btn v-if="isDisabled" class="ma-2" color="indigo" large outlined dark v-on="on">MY INFO</v-btn>
                        <v-btn v-else class="ma-2" color="indigo" large outlined dark @click="login()"> kakao</v-btn>
                </template>
      
    </v-dialog>

    <v-dialog v-model="dialog" persistent max-width="600px">
                <template v-if="isDisabled" v-slot:activator="{ on }">
                <v-btn class="ma-2" color="indigo" large outlined dark @click="logout()"> logout</v-btn>     
</template>
      <v-card>
        <v-card-title>
          <span class="headline">LoginModal</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            회원가입 해보렴
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
          <v-btn color="blue darken-1" text @click="dialog = false">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  
    </v-app-bar>
</template>


<script>
import {
    mapGetters
} from 'vuex';
import axios from "axios";
export default {
    computed: {
        ...mapGetters(['links'])
    },
    
    mounted(){
        console.log(this.$route.query)
        var token = this.$route.query.access_Token
        if(token!=undefined){
            this.$session.start()
            this.$session.set('token', token)
            console.log("token:"+this.$session.get('token'))
        }
        if(this.$session.get('token')!=undefined){
            console.log("session:"+this.$session.get('token'))
        }
    },
    methods: {
        login() {
            window.location.href = "https://kauth.kakao.com/oauth/authorize?client_id=caca7722fcbd20626b2343a0f5bf4083&redirect_uri=http://localhost:8080/login&response_type=code"
        },
        logout(){

            axios.get('localhost:8080/logout')
            .then(response=>{
                console.log(response)
                this.$session.destroy()
                let query  = Object.assign({}, this.$route.path)
                console.log(query)
                this.$router.push({ query })
            }).catch(err=>{
                console.log(err)
            })
        },
        isDisabled(){
            if(this.$session.get('token')!=undefined){
                return true;
            }
            return false;
        },
        gotoHome(e) {
            e.stopPropagation()
            if (this.$route.path === "/") {
                this.$vuetify.goTo(0)
                //window.location.reload()
                return
            }
            this.$router.push("/", () => {});
            return;
        },
        search(e) {
            e.stopPropagation()

            if (e.keyCode === 13) {
                this.$router.push({ path: '/searchPage', query: { word: this.searchWord } }, () => {});
                this.searchWord = ""

            }

        },
        onScroll() {
            var scroll = window.pageYOffset
            var value = "#cdcdcd"
            var position = 250
            if (scroll >= position) {
                value += "ff"
            } else {
                var tmp = Math.round((scroll / position * parseInt("FF", 16))).toString(16);
                if (tmp.length == 1) {
                    value += "0" + tmp
                } else {
                    value += tmp
                }


            }

            this.headerColor = value

        }


    },
    data() {
        return {
            searchWord: "",
            dialog: false,
            headerColor: "transparent"

        };
    },
    creted() {
        this.headerColor = "#00000000"
        
    }


}
</script>

<style scoped>
#header {
    background-color: #999999;
    position: absolute;
}

.v-toolbar__content,
.v-toolbar__extension {
    background-color: blue;
    color: blue
}

.app_bar_tt {
    background-color: blue;
}

.disable-events {
    pointer-events: none
}
</style>