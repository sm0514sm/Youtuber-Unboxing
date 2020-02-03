<template>
  <v-menu open-on-hover top offset-y :nudge-width="200" :nudge-top="20" :close-delay="300">
    <template v-slot:activator="{ on, attrs }">
      <v-btn v-bind="attrs" v-on="on" fab fixed bottom right></v-btn>
    </template>

    <v-list>
      <v-list-item>
        <v-card>
          왜 안되냐...
          <div v-for="(item,index) in youtubers" :key="index">
            {{item}}
          </div>
        </v-card>
      </v-list-item>
      <v-list-item>
        <v-card>최근 본 유튜버</v-card>
      </v-list-item>
    </v-list>
  </v-menu>
</template>

<script>

export default {
  computed: {
    youtubers : function() {
      var output = localStorage.getItem("compareYoutuber");		
      var arr = JSON.parse(output);
      console.log(arr)
      return arr;
    }
  },
  watch: {
    [localStorage.getItem("compareYoutuber")] : function(){
      var output = localStorage.getItem("compareYoutuber");		
      var arr = JSON.parse(output);
      console.log("watch"+arr)
      return arr;
    }

  },
  methods: {
  },
  created(){
    console.log(this);
  },
  data: () => ({
    items: [
      { title: "Click Me" },
      { title: "Click Me" },
      { title: "Click Me" },
      { title: "Click Me 2" }
    ]
  })
};
</script>

