<template>
  <div id="app">
    <Map name="This is our map collection:"/>
  </div>
</template>

<script>
import Map from "./components/Map.vue"
export default {
  name: 'app',
  components: {
    Map,
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
