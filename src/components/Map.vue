<template>
  <b-container class="map">
    <h3>{{name}}</h3>
    <div class="card" style="width: 18rem;">
      <div class="card-header bg-primary text-white">
        Layers <v-icon class="float-right" name="layer-group"/>
      </div>
      <b-list-group>
        <draggable v-model="layers">
          <Layer v-for="item in layers" v-bind:layer="item" :key="item.id" :visible="item.visible">
          </Layer>
        </draggable>
      </b-list-group>
    </div>
  </b-container>
</template>

<script>
import Layer from "./Layer.vue";
import draggable from 'vuedraggable';
import jsonData from "../assets/layers.json";
export default {
  name: "Map",
  components: { Layer, draggable },
  props: {
    name: String
  },
  data() {
    return {
      layers: jsonData
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 1em 0 1em;
}
</style>
