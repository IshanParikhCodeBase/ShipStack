<script setup lang="ts">

defineProps<{ msg: string }>()


</script>

<template>
  <div class="main-box">
    <div class="origin-box">
      <h2>Enter your store location: </h2>
      <input type="text">
    </div>
    <div class="destinations">
      <h2>Enter your destinations (CSV): </h2>
      <input type="text">
    </div>
    <br>
    <button id="btn-cluster">Get Clusters</button>
  </div>
</template>

<style scoped>

</style>
