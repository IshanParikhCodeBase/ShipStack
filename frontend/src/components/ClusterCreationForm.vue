<!-- ----------------------------------- SCRIPT -------------------------------------->
<script setup lang="ts">
import {clusterData,Cluster} from '../components/data_management'
import axios from "axios";
import * as XLSX from "xlsx";
import ClusterCard from "../components/ClusterCard.vue";
import DestinationsCard from "../components/DestinationsCard.vue";


 const fetchClusters = async () => {
    const jsonData = {
      destinations: clusterData.destinations,
      origin: clusterData.origin,
    };

    try {
      console.log(jsonData);
      const response = await axios.post(
        "http://127.0.0.1:8000/uploadAddr",
        jsonData
      );

      clusterData.clusters = JSON.parse(response.data);
      console.log(clusterData.clusters);
    } catch (error) {
      console.error("Error fetching posts:", error);
    }
  }; //end of fetch clusters

  const flatten = (data: [Cluster]) => {
    const flattened = [] as any;
    data.forEach((item) => {
      item.locations.forEach((location) => {
        flattened.push({
          groupName: "Group " + item.groupName,
          location: location,
        });
      });
    });
    return flattened;
  }; //end of flatten

  const downloadAsExcel = () => {
    const flattenedData = flatten(clusterData.clusters as [Cluster]);

    const worksheet = XLSX.utils.json_to_sheet(flattenedData);
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, "Clusters");
    XLSX.writeFile(workbook, "shipping_groups.xlsx");
  }; //end of downloadExcel



</script>
<!-- ----------------------------------- HTML BODY -------------------------------------->
<template>
  <center><h1 id="main-header">ShipStack</h1></center>
  <div class="main-box">
    <div class="origin-box card">
      <h2>Enter your store location:</h2>
      <input
        class="input-text"
        v-model="clusterData.origin"
        type="text"
        placeholder="Enter address"
      />

      <!-- <p>Origin: {{ origin }}</p> -->
    </div>
    <DestinationsCard  />
    <br />
    <center>
      <button class="btn-cluster" id="btn-get-clusters" @click="fetchClusters()">
        Get Clusters
      </button>
    </center>
  </div>
  <div id="response p-4 w-max">
    <ClusterCard
      v-for="c in clusterData.clusters"
      :key="c.groupName"
      :locations="c.locations"
      :clusterNumber="c.groupName"
    />
  </div>
  <center>
    <button
      class="btn-cluster"
      id="btn-download-as-excel"
      @click="downloadAsExcel()"
    >
      Download as Excel
    </button>
  </center>
</template>
<!-- ----------------------------------- STYLING -------------------------------------->
<style>
:root {
  --color-light: white;
  --color-dark: #212121;
  --color-signal: #fab700;

  --color-background: var(--color-light);
  --color-text: var(--color-dark);
  --color-accent: var(--color-signal);

  --size-bezel: 0.2rem;
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

#main-header {
  font-size: 2em;
}

.input-text {
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

.btn-cluster {
  margin: 1em;
  color: currentColor;
  padding: var(--size-bezel) calc(var(--size-bezel) * 2);
  background: var(--color-light);
  border: #212121 solid 3px;
  border-radius: var(--size-radius);
}

.btn-cluster + .btn-cluster {
  margin-left: calc(var(--size-bezel) * 2);
}

.hidden {
  display: none;
}
</style>
