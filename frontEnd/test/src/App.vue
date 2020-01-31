<template>
  <v-app id="app">
    
    <header-component></header-component>

    <v-content>
      <router-view />
    </v-content>

    <footer-component></footer-component>
    
      <compare-component />
  </v-app>
</template>

<script>

export default {
  name: "app",
  components: {
  },
    data () {
      return {
      //
      }
    }
};
</script>
