<template>
    <v-app-bar id="app_bar_tt" :color="headerColor"  fixed elevate-on-scroll scroll-threshold="500"  v-scroll="onScroll"

>
    
    
        <v-img :src="require('@/assets/logo.png')" class="" contain height="48" width="48" max-width="48" @click="gotoHome" />
    
        <v-spacer />
    
        <v-toolbar-title> Test
        </v-toolbar-title>
    
    
        <v-spacer />
    
    
        <v-text-field append-icon="mdi-magnify" flat hide-details solo-inverted style="max-width: 300px; " @keyup.enter="search" v-model="searchWord" :key="$route.fullPath" />
    
        <v-row justify="center">
            <v-dialog v-model="dialog" persistent max-width="600px">
                <template v-slot:activator="{ on }">
                    <v-btn color="primary" dark v-on="on">login</v-btn>
            </template>
      <v-card>
        <v-card-title>
          <span class="headline">LoginModal</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            login 해보렴
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
  </v-row>
    </v-app-bar>
</template>


<script>
import {
    mapGetters
} from 'vuex'

export default {
    computed: {
        ...mapGetters(['links'])
    },
    methods: {
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
            var position = 350
            if(scroll >= position){
                value += "ff"
            }else{
                var tmp = Math.round((scroll/position*parseInt("FF", 16))).toString(16);
                if(tmp.length == 1){
                    value += "0" + tmp
                }else{
                    value +=  tmp
                }


            }
           
             this.headerColor = value
            
        }


    },
    data() {
        return {
            searchWord: "",
            dialog: false,
            headerColor : "transparent"

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
.v-toolbar__content, .v-toolbar__extension  {
    background-color: blue;
    color : blue
}
.app_bar_tt{
    background-color: blue;
}

.disable-events {
    pointer-events: none
}
</style>