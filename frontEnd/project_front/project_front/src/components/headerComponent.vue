<template>
    <v-app-bar id="app_bar_tt" :color="headerColor" fixed elevate-on-scroll scroll-threshold="500" v-scroll="onScroll">
        <v-img :src="require('@/assets/logo.png')" class="" contain height="48" width="48" max-width="48" @click="gotoHome" />

        <v-spacer />
        <v-text-field class="ma-2" append-icon="mdi-magnify" flat hide-details solo-inverted style="max-width: 300px; " @keyup.enter="search" v-model="searchWord" :key="$route.fullPath" />
        <v-img v-if="!loginStatus" :src="require('@/assets/kakao.png')" class="" contain height="100" width="100" max-width="100" @click="login()"/>

        <v-dialog v-model="dialog" persistent max-width="600px">
            <template v-if="loginStatus" v-slot:activator="{ on }">  
                <v-btn class="ma-2" color="indigo" large outlined dark v-on="on">LOGOUT</v-btn>
                <v-btn class="ma-2" color="indigo" large outlined dark @click="gotoMember()">MY INFO</v-btn>
            </template>
            <v-card>
            <v-card-title>
                <span class="headline">LogoutModal</span>
            </v-card-title>
            <v-card-text>
                <v-container>
                정말로 로그아웃 하겠습니까?
                </v-container>
                <small>*indicates required field</small>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="dialog = false">No</v-btn>
                <v-btn color="blue darken-1" text @click="logout()">Yes</v-btn>
            </v-card-actions>
            </v-card>
        </v-dialog>
    </v-app-bar>
</template>


<script>
import {
    mapGetters
} from 'vuex';
// import axios from "axios";
export default {
    computed: {
        ...mapGetters(['links'])
    },
    
    mounted(){
        console.log("loginStatus:"+this.loginStatus)
        if (!this.$session.exists()) {
            this.loginStatus=false
            console.log("no session")
        }
        console.log(this.$route.query)
        var token = this.$route.query.access_Token
        if(token!=undefined){
            this.$session.start()
            this.$session.set('token', token)
            this.loginStatus=true
            console.log("token:"+this.$session.get('token'))
            this.$router.push('/')
        }
    },
    methods: {
        gotoMember(){
            this.$router.push("/memberPage");
        },
        login() {
            window.location.href = "https://accounts.kakao.com/login?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fclient_id%3Dcaca7722fcbd20626b2343a0f5bf4083%26redirect_uri%3Dhttp%3A%2F%2Flocalhost%3A8080%2FSpringBoot%2Flogin%26response_type%3Dcode"
        },
        logout(){
            this.$session.destroy()
            console.log(this.$route.query)
            if(this.$route.path=='/memberPage'){
                this.$router.push('/')
            }
            window.location.reload()
            
            // axios.get('localhost:8080/logout')
            // .then(response=>{
            //     console.log(response)
            //     this.$session.destroy()
            //     let query  = Object.assign({}, this.$route.path)
            //     console.log(query)
            //     this.$router.push({ query })
            // }).catch(err=>{
            //     console.log(err)
            // })
        },
        isDisabled(){
            return true;
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
            loginStatus: true,
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