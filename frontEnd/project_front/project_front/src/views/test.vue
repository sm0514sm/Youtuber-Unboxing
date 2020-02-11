<template>
  <v-container>
    <v-row>
      <v-col
        v-for="(item, $index) in videolist"
        :key="$index"
        :data-num="$index + 1"
        class="pa-1"
        cols="6"
      >
        <v-row>
          <v-col>
            <iframe
              :src="String('https://www.youtube.com/embed/')+item.videoID"
              frameborder="0"
              allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen
            ></iframe>
          </v-col>
        </v-row>
        <v-row><p class="text-truncate">{{item.videoName}}</p></v-row>
      </v-col>
    </v-row>
    <infinite-loading @infinite="infiniteHandler"></infinite-loading>
  </v-container>
</template>


<script>
import axios from "axios";
import InfiniteLoading from "vue-infinite-loading";

const api = "http://15.165.77.1:8080/SpringBootNew/youtuber/detail/video/597";

export default {
  name: "TestPage",
  components: {
    InfiniteLoading
  },
  methods: {
    infiniteHandler($state) {
      var range = 10;
      var rawList = [];
      axios.get(api).then(({ data }) => {
        rawList = data.data;
        var tmplist = rawList.slice(
          this.page * range,
          this.page * range + range
        );
        if (tmplist.length > 0) {
          this.page += 1;
          this.videolist.push(...tmplist);
          $state.loaded();
        } else {
          $state.complete();
        }
      });
    }
  },
  data() {
    return {
      page: 0,
      videolist: []
    };
  },
  created() {}
};
</script>

<style scoped>
</style>