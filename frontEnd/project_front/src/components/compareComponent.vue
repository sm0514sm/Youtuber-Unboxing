<template>
  <v-menu open-on-hover top offset-y :nudge-width="200" :nudge-top="20" :close-delay="300">
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        v-bind="attrs"
        v-on="on"
        fab
        fixed
        bottom
        right
      >
        
      </v-btn>
    </template>

    <v-list>
      <v-list-item >
        <v-card>
          <v-img
          :src="require('@/assets/logo.png')"
          class=""
          contain
          height="300"
          width="300"
          max-width="300"
        />
        <span> 비교하기 기능을 위한 menu </span>
        </v-card>
        
      </v-list-item>
      
    </v-list>
  </v-menu>
</template>

<script>
  export default {
    data: () => ({
      items: [
        { title: 'Click Me' },
        { title: 'Click Me' },
        { title: 'Click Me' },
        { title: 'Click Me 2' }
      ]
    })
  }
</script>

