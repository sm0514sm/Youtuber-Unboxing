<template>
  <div>
    <v-card>
      <v-card-title class="justify-center py-6" style="background-color:#cdcdcd ; height : 300px">
        <i class="font-weight-black display-3">CATEGORY</i>
      </v-card-title>
    </v-card>
    <v-divider></v-divider>
    <v-container name="container">
      <v-tabs v-model="currentCategory" background-color="transparent" color="basil" grow>
        <v-tab
          v-for="(item,index) in categories"
          :key="index"
          @click="onCategoryButtonClicked(index)"
        >{{ item. nameEng}}</v-tab>
      </v-tabs>
      <v-divider></v-divider>
      <v-tabs-items v-model="currentCategory">
        <v-tab-item v-for="(item,index) in categories" :key="index">
          <v-card flat class="pa-3">
            <v-card
              v-for="(item,index) in youtubersPerCategory"
              :key="index+100"
              class="ma-5"
              flat
              outlined
            >
              <v-data-table
                v-model="selected"
                :headers="headers"
                :items="desserts"
                :single-select="singleSelect"
                item-key="name"
                show-select
                class="elevation-1"
              >
              
              </v-data-table>
              <!-- <v-container>
                <v-row>
                  <v-col justify="space-between" :cols="4">
                    <v-col>
                      <v-card
                        :img="item.thumbnails"
                        :to="{ path: 'youtuberPage', query: { yno : item.yno}}"
                        flat
                      >
                        <v-responsive :aspect-ratio="1/1"></v-responsive>
                      </v-card>
                    </v-col>
                  </v-col>
                  <v-col :cols="7" class="ma-3">
                    <v-row>
                        <p class="font-weight-light display-3">{{item.channelName}}</p>
                    </v-row>
                    <v-row>{{item.channelDescription}}</v-row>
                    <v-row>{{item.regDate}}</v-row>
                  </v-col>
                </v-row>
              </v-container>-->
            </v-card>
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
      this.$store.state.currentCategory = index;
      this.$store.dispatch(Constant.GET_YOUTUBERS_PER_CATEGORY, {
        category: this.findCano()
      });
    },
    findCano: function() {
      return this.categories[this.$store.state.currentCategory].cano;
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
      return Number(this.$store.state.currentCategory);
    }
  },
  watch: {},
  data() {
    return {};
  }
};
</script>

<style scoped>
</style>
