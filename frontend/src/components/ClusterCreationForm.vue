<script setup lang="ts">
import { ref } from "vue";
import axios from "axios";
import ClusterCard from "../components/ClusterCard.vue";

const clusters = ref([]);
const destinations = ref("");
const origin = ref("");

const fetchClusters = async () => {
  const jsonData = {
    destinations: destinations.value,
    origin: origin.value,
  };

  // console.log('Dest: '+destinations.value)
  // console.log('origin'+origin.value)
  // console.log(jsonData)

  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/uploadAddr",
      jsonData
    );
    clusters.value = JSON.parse(response.data);
  } catch (error) {
    console.error("Error fetching posts:", error);
  }
};
</script>

<template>
     <center> <h1 id="main-header">ShipStack</h1></center>
  <div class="main-box">

    <div class="origin-box card">
      <h2>Enter your store location:</h2>
      <input class="input-text" v-model="origin"  type="text" />
      <p>Origin: {{ origin }}</p>
    </div>
    <div class="destinations card">
      <h2>Enter your destinations (CSV):</h2>
      <input class="input-text" v-model="destinations" type="text" />
      <p>Destinations: {{ destinations }}</p>
    </div>
    <br />
    <center><button id="btn-cluster" @click="fetchClusters">Get Clusters</button></center> 
  </div>
  <div id="response p-4 w-max">
    <ClusterCard
      v-for="(c, index) in clusters"
      :key="c"
      :locations="c"
      :clusterNumber="index.toString()"
    />
  </div>
</template>

<style>
:root {
  --color-light: white;
  --color-dark: #212121;
  --color-signal: #fab700;

  --color-background: var(--color-light);
  --color-text: var(--color-dark);
  --color-accent: var(--color-signal);

  --size-bezel: 0.5rem;
  --size-radius: 4px;

  line-height: 1.4;

  font-family: "Inter", sans-serif;

  color: var(--color-text);
  background: var(--color-accent);
  font-weight: 300;
  padding: 0 calc(var(--size-bezel) * 3);
}

h1,
h2,
h3 {
  font-weight: 900;
}

#main-header{
  font-size: 2em;
}

.input-text{

  border: solid black 2px;
  border-radius: 2px;
}

.card {
  background: var(--color-background);
  padding: calc(4 * var(--size-bezel));
  margin-top: calc(4 * var(--size-bezel));
  border-radius: var(--size-radius);
  border: 3px solid var(--color-shadow, currentColor);
  box-shadow: 0.5rem 0.5rem 0 var(--color-shadow, currentColor);

  &--inverted {
    --color-background: var(--color-dark);
    color: var(--color-light);
    --color-shadow: var(--color-accent);
  }

  &--accent {
    --color-background: var(--color-signal);
    --color-accent: var(--color-light);
    color: var(--color-dark);
  }

  *:first-child {
    margin-top: 0;
  }
}


.button-group {
  margin-top: calc(var(--size-bezel) * 2.5);
}

.main-box #btn-cluster {
  color: currentColor;
  padding: var(--size-bezel) calc(var(--size-bezel) * 2);
  background: var(--color-light);
  border: #212121 solid 3px;
  border-radius: var(--size-radius);
 


}

.main-box #btn-cluster + #btn-cluster {
  margin-left: calc(var(--size-bezel) * 2);
}

.hidden {
  display: none;
}
</style>
