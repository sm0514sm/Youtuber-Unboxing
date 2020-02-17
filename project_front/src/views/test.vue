<template>
  <div>
    <br />
    <br />
    <br />
    <br />
    <v-btn>TEST</v-btn>
    <v-btn disabled>TEST</v-btn>
    <v-btn disabled="true">TEST</v-btn>
    <v-btn disabled="false">TEST</v-btn>
    <v-btn :disabled="test">TEST</v-btn>
  </div>
</template>


<script>
// Load on demand

export default {
  components: {},
  data() {
    return {};
  },
  methods: {
    test() {
      return false
    }
   
  },
  mounted() {
    
  }
};
</script>
<style scoped>
</style>