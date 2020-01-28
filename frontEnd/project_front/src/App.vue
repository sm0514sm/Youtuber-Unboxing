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
import headerComponent from "./components/headerComponent";
import footerComponent from "./components/footerComponent";
import compareComponent from "./components/compareComponent";

export default {
  name: "app",
  components: {
    headerComponent, footerComponent, compareComponent,
  },
    data () {
      return {
      //
      }
    }
};
</script>
