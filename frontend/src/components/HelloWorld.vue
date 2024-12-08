<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';

const clusters = ref([]);
const destinations = ref('');
const origin = ref('');

const fetchClusters = async () => {

  const jsonData = {
    destinations: destinations.value,
    origin:origin.value
  };

  console.log('Dest: '+destinations.value)
  console.log('origin'+origin.value)
  console.log(jsonData)

  try {
    const response = await axios.post('http://127.0.0.1:8000/uploadAddr',jsonData);
    clusters.value = response.data;
  } catch (error) {
    console.error('Error fetching posts:', error);
  }
};

</script>

<template>
  <div class="main-box">
    <div class="origin-box">
      <h2>Enter your store location: </h2>
      <input v-model="origin" type="text">
      <p>Origin: {{origin}}</p>
    </div>
    <div class="destinations">
      <h2>Enter your destinations (CSV): </h2>
      <input v-model="destinations" type="text">
      <p>Destinations: {{destinations}}</p>
    </div>
    <br>
    <button id="btn-cluster" @click="fetchClusters">Get Clusters</button>
  </div>
  <div id="response">
    <p>{{clusters}}</p>
  </div>
</template>

<style scoped>

</style>
