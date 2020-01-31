<template>
  <div>
    <v-card>
      <v-card-title class="justify-center py-6" style="background-color:#cdcdcd ; height : 300px">
        <i class="font-weight-black display-3">CATEGORY</i>
      </v-card-title>
    </v-card>
    <v-container name="container" background-color="transparent">
      <v-tabs :value="currentCategory" background-color="transparent" grow>
        <v-tab
          v-for="(item,index) in categories"
          :key="index"
          @click="onCategoryButtonClicked(index)"
        >{{ item. nameEng}}</v-tab>
      </v-tabs>
      <v-tabs-items :value="currentCategory" >
        <v-tab-item v-for="(item,index) in categories" :key="index"  >
          <v-card flat class="pa-3" color="#FAFAFA">
            <v-data-table flat :headers="headers" :items="youtubersPerCategory" class="elevation-1" hide-default-footer>

              <template v-slot:item.thumbnails="{ item }">
                <v-card color="#00000000" flat :to="{ path: 'youtuberPage', query: { yno : item.yno}}">
                  <v-row>
                    <v-col cols="4">
                      <v-card color="#00000000"   width="50px" flat>
                        <v-responsive :aspect-ratio="1/1">
                          <v-img class="circle" :src="item.thumbnails" flat/>
                        </v-responsive>
                      </v-card>
                      <!-- <v-card  :img="item.thumbnails" flat width="50px">
                        <v-responsive :aspect-ratio="1/1"></v-responsive>
                      </v-card> -->
                    </v-col>
                    <v-col cols="8" >
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
          </v-card>
        </v-tab-item>
      </v-tabs-items>
    </v-container>
    
  </div>
</template>


<script>
import { mapGetters } from "vuex";
import Constant from "../vuex/Constant";

export default {
  components: {},
  name: "categoryPage",

  methods: {
    onCategoryButtonClicked(index) {
      localStorage.setItem('currentCategory',index)
      this.$store.dispatch(Constant.GET_YOUTUBERS_PER_CATEGORY, {
        category: this.findCano()
      });
    },
    findCano: function() {
      return this.categories[localStorage.getItem('currentCategory')].cano;
    }
  },
  mounted() {
    this.$vuetify.goTo(0);
  },
  created() {

    this.$store.dispatch(Constant.GET_YOUTUBERS_PER_CATEGORY, {
      category: this.findCano()
    });
  },
  computed: {
    ...mapGetters(["categories"]),
    ...mapGetters(["youtubersPerCategory"]),
    currentCategory() {
      return Number(localStorage.getItem('currentCategory'));
    }
  },
  watch: {},
  data() {
    return {
      headers: [
        { text: "", value: "thumbnails", sortable: false },
        { text: "subscriber", value: "subscriber" },
        { text: "influence", value: "influence" },
        { text: "activity", value: "activity" },
        { text: "growth", value: "growth" },
        { text: "basicStat", value: "basicStat" },
        { text: "charm", value: "charm" },
        { text: "grade", value: "grade" }
      ]
    };
  }
};
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
</style>
