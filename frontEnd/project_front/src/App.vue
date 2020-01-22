<template>
  <v-app id="app">
    <header-component></header-component>
    <router-view />
    <footer-component></footer-component>
  </v-app>
</template>

<script>
import headerComponent from "./components/headerComponent";
import footerComponent from "./components/footerComponent";

export default {
  name: "app",
  components: {
    headerComponent, footerComponent,
  },
    data () {
      return {
      //
      }
    }
};
</script>
