<template>
  <li class="layer"><a v-bind:href="layer.url">{{layer.name}}</a></li>
</template>

<script>
export default {
  name: "Layer",
  props: ['layer']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
li {
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
