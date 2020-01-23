<template>
    <v-container wrap style="background : gray">
      <h1> hello {{selectedCategory}} </h1>
      <v-card v-for="(item,i) in youtubersPerCategory" :key=i class="ma-5" >
        <v-container>
          <v-row>
          <v-col justify="space-between">
            <v-col width>
              <v-img
                height="200"
                width="200"
                :src="item.thumbnails"
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
</template>


<script>
  import Constant from"../vuex/Constant";
  import {
    mapGetters
}from 'vuex'

  export default {
    data () {
      return {
        
      }
    },
    watch :{
      
      selectedCategory : function() {
        console.log("categoryComponent_watch"+this.selectedCategory);
        
        this.$store.dispatch(Constant.GET_YOUTUBERS_PER_CATEGORY, {
          category : this.findCano()
        })
      }
    },
    props : {
      selectedCategory : {default:"game"},  
    },
    computed : {
      ...mapGetters(['categories']),
      ...mapGetters(['youtubersPerCategory']),
    },
    methods : {
      findCano : function() {
        for (var value of this.categories) {
          if(value.nameEng === this.selectedCategory){
            return value.cano
          }
        }
        return 1;
      }
    }
  }
</script>

<style scoped>

</style>