<script setup lang="ts">

const props = defineProps({
    clusterNumber: {
        type: String,
        default: "no name",
        required: true
    },
    locations: {
        type: Array<string>, 
        default: () => [] 
    },
});

console.log(props)
</script>

<template>
    <div class="card">
      <h2 class="cluster-header">
        {{ props.clusterNumber == "-1" ? "Outlier(s)" : "Group " + props.clusterNumber }}
      </h2>
      <ul>
        <li class="location" v-for="l in props.locations" :key="l">
          {{ l }}
        </li>
      </ul>
    </div>
  </template>

<style scoped>

    .cluster-header{
        margin-bottom: 0.25rem; 
        color: black; 
        font-size: 1.125rem; 
    }

    .location{
        color: #5a5a5a; 
        display: flex; 
        width: 100%; 
        align-items: center; 
        border-radius: 0.25rem;
        padding: 0.25rem; 
        transition: all 0.15s ease-in-out; 
   

        &:hover, &:focus, &:active {
        background-color: #dfdfdf;
    }
}

</style>
