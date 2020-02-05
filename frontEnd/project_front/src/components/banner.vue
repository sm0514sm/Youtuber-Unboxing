<template>
  <v-carousel cycle height="400" hide-delimiter-background show-arrows-on-hover>
    <v-carousel-item v-for="(slide, i) in slides" :key="i" interval="10">
      <v-sheet color="transparent" height="100%">
        <!-- table -->
        <v-row class="fill-height" align="center" justify="center">
          <div>
            <v-simple-table light>
              <template v-slot:default>
                <tbody>
                  <tr v-for="item in youtuber_stat" :key="item.name" @click="test">
                    <td><v-btn>안녕</v-btn></td>
                    <td>{{ item.name }}</td>
                    <td>{{ item.figure1 }}</td>
                  </tr>
                </tbody>
              </template>
            </v-simple-table>
          </div>
          <div class="display-3">{{ slide }} Slide</div>
        </v-row>
      </v-sheet>
    </v-carousel-item>
  </v-carousel>
</template>


<script>
export default {
  data() {
    return {
      colors: [
        "indigo",
        "warning",
        "pink darken-2",
        "red lighten-1",
        "deep-purple accent-4"
      ],
      slides: ["First", "Second", "Third", "Fourth", "Fifth"],
      youtuber_stat : []
    };
  },
  created() {
    //render table
      this.youtuber_stat = [
        { name: "영향력", figure1: 1},
        { name: "활동력", figure1: 2 },
        { name: "성장력", figure1: 3  },
        { name: "기본수치", figure1: 4},
        { name: "매력", figure1: 5 }
      ];
  },
  methods: {
    test : function(e) {
     
      console.log("hi")
    }
  }
};
</script>

<style scoped>
</style>