<!-- ----------------------------------- SCRIPT -------------------------------------->
<script setup lang="ts">

import {clusterData} from '../components/data_management'
import 'primeicons/primeicons.css'

  const addDestinations = () => {
    if (clusterData.newDestination) {
      clusterData.destinations.push(clusterData.newDestination);
      clusterData.newDestination = "";
      
    }
  };
  const deleteDestination = (index: number)=>{
    clusterData.destinations.splice(index, 1);
  };

</script>
<!-- ----------------------------------- HTML BODY -------------------------------------->
<template>
<div class="destinations card">
      <h2>Enter your destinations:</h2>
      <input
        class="input-text"
        v-model="clusterData.newDestination"
        type="text"
        placeholder="Enter an address"
        @keyup.enter="addDestinations()"
      />
      <!-- <p>Destinations: {{ destinations }}</p> -->
      <button
        @click="addDestinations()"
        class="btn-dest"
        id="btn-add-destinations"
      >
        <i class="pi pi-plus-circle"></i>
      </button>
      <ul>
        <li v-for="(dest, index) in clusterData.destinations" :key="index">
          {{ dest }}
          <button
            @click="deleteDestination(index)"
            class="btn-dest"
            id="btn-delete-destinations"
          >
            <i class="pi pi-trash"></i>
          </button>
        </li>
      </ul>
    </div>

</template>
<!-- ----------------------------------- STYLING -------------------------------------->
 <style>

.btn-dest{
  padding: 5px;
  margin: 1em;
  border-width: 2px;
  border: #212121 solid 2px;
  border-radius: var(--size-radius);
}
 #btn-delete-destinations{
  background-color: rgba(215, 11, 11, 0.858);
 }
 #btn-add-destinations{
  background-color: rgba(21, 231, 21, 0.764);


}

</style>