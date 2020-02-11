<template>
  <div>
    <br />
    <br />
    <br />
    <v-autocomplete
      :items="searchItems"
      hide-details
      item-text="channelName"
      item-value="channelName"
      :search-input.sync="inputKeyword"
      solo
      @keyup.enter="search"
      ref="keyword"
      id = "keyword"
      label="유튜버를 검색해보세요"
      style="max-width: 300px; "
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
          <v-list-item-subtitle>{{item.subscriber}}</v-list-item-subtitle>
        </v-list-item-content>
      </template>
    </v-autocomplete>
  </div>
</template>


<script>
import http from "../vuex/http-common";
export default {
  name: "TestPage",
  components: {},
  data: () => ({
    searchItems: [],
    inputKeyword: null,
  }),
  created() {
http
        .get("/youtuber/all")
        .then(response => {
          console.log(response.data.data);
          this.searchItems = response.data.data;
        })
        .catch(err => {
          console.log(err);
        })
  },

  watch: {
    
    inputKeyword() {
      // Items have already been loaded
      if (this.searchItems.length > 0) return;


      // Lazily load input items
      http
        .get("/youtuber/all")
        .then(response => {
          console.log(response.data.data);
          this.searchItems = response.data.data;
        })
        .catch(err => {
          console.log(err);
        })
    }
  },
  methods: {
    search: function() {
      console.log("*************"+document.getElementById("keyword").value)
      this.$router.push(
        { path: "/searchPage", query: { word: document.getElementById("keyword").value } },
        () => {}
      );
    },
  }
};
</script>

<style scoped>
</style>