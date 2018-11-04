<template>
  <b-container class="map">
    <b-row>
      <b-col cols="4">
        <div class="card">
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
      </b-col>
      <b-col>
        <l-map :zoom="zoom" :center="center" style="height: 100%">
          <l-tile-layer 
            url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"
            attribution= '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          />
        </l-map>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import Layer from "./Layer.vue";
import draggable from "vuedraggable";
import jsonData from "../assets/layers.json";
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import { LMap, LTileLayer } from "vue2-leaflet";

export default {
  name: "Map",
  components: { Layer, draggable, LMap, LTileLayer },
  props: {
    name: String
  },
  data() {
    return {
      zoom: 3,
      center: L.latLng(20, 20),
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
