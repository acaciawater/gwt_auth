<template>
  <div class="map">
    <h3>{{name}}</h3>
    <ul>
      <Layer v-for="item in layers" v-bind:layer="item" :title="item.url" :key="item.id">
      </Layer>
    </ul>
  </div>
</template>

<script>
import Layer from "./Layer.vue";
export default {
  name: "Map",
  components: { Layer },
  props: {
    name: String
  },
  data() {
    return {
      layers: [
        { id: 0, name: "Stress", url: "https://example.com" },
        { id: 1, name: "Recharge", url: "https://example.com" },
        { id: 2, name: "Landuse", url: "https://example.com" }
      ]
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
</style>
