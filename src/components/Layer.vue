<template>
  <b-list-group-item button v-on:click="layer.visible=!layer.visible">
    <v-icon class="left" name="eye" v-show="layer.visible" />
    <span class="name">{{layer.name}}</span>
    <a href="#"><v-icon class="right" name="ellipsis-h" /></a>
  </b-list-group-item>
</template>

<script>
export default {
  name: "Layer",
  props: ["layer"]
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
  color: #4297b9;
}

.left {
  position: absolute;
  left: 1em;
  top: 1em;
}

.right {
  position: absolute;
  right: 1em;
  top: 1em;
}

.name {
  position: relative;
  left: 2em;
}
</style>
