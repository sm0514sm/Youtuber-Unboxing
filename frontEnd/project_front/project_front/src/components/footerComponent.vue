<template>
  <v-footer dark padless>
    <v-card flat tile class="indigo lighten-1 white--text text-center">
      <v-card-text>
        <v-btn v-for="icon in icons" :key="icon" class="mx-4 white--text" icon>
          <v-icon size="24px">{{ icon }}</v-icon>
        </v-btn>
      </v-card-text>

      <v-card-text
        class="white--text pt-0"
      >Phasellus feugiat arcu sapien, et iaculis ipsum elementum sit amet. Mauris cursus commodo interdum. Praesent ut risus eget metus luctus accumsan id ultrices nunc. Sed at orci sed massa consectetur dignissim a sit amet dui. Duis commodo vitae velit et faucibus. Morbi vehicula lacinia malesuada. Nulla placerat augue vel ipsum ultrices, cursus iaculis dui sollicitudin. Vestibulum eu ipsum vel diam elementum tempor vel ut orci. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</v-card-text>

      <v-divider></v-divider>

      <v-card-text class="white--text">
        {{ new Date().getFullYear() }} —
        <strong>Vuetify</strong>
      </v-card-text>
    </v-card>
  </v-footer>
  <!-- <v-footer
    class="py-4"
    dark
    height="auto"
  >
    <v-container mx-auto>
      <v-layout wrap>
        <v-flex xs9>
            <i class="font-weight-black ">김주희, 김태민, 박진홍, 이상민, 홍기환</i>
        </v-flex>
        <v-spacer />
        <v-btn
          class="mr-0"
          square
          
          @click="$vuetify.goTo(0)"
        >
          <v-icon>mdi-chevron-up</v-icon>
        </v-btn>
      </v-layout>
    </v-container>
  </v-footer>-->
</template>

<script>
export default {
  data: () => ({
    icons: [
      "fa-facebook",
      "fa-twitter",
      "fab fa-google-plus",
      "fab fa-linkedin",
      "fab fa-instagram"
    ]
    // items: [
    //   {
    //     href: "#!",
    //     icon: "mdi-twitter"
    //   },
    //   {
    //     href: "#!",
    //     icon: "mdi-instagram"
    //   },
    //   {
    //     href: "#!",
    //     icon: "mdi-facebook"
    //   },
    //   {
    //     href: "#!",
    //     icon: "mdi-google-plus"
    //   },
    //   {
    //     href: "#!",
    //     icon: "mdi-reddit"
    //   },
    //   {
    //     href: "#!",
    //     icon: "mdi-discord"
    //   },
    //   {
    //     href: "#!",
    //     icon: "mdi-pinterest"
    //   }
    // ]
  })
};
</script>

<style scoped>
</style>