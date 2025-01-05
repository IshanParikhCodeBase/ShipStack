<script setup lang="ts">
import {clusterData,Cluster} from '../components/data_management'
import * as XLSX from "xlsx";
import ClusterCard from "./ClusterCard.vue";
import DestinationsCard from "./DestinationsCard.vue";


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
};

const downloadAsExcel = () => {
    const flattenedData = flatten(clusterData.clusters as [Cluster]);
    const worksheet = XLSX.utils.json_to_sheet(flattenedData);
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, "Clusters");
    XLSX.writeFile(workbook, "shipping_groups.xlsx");
};


</script>

<template>
    <div class="form-container">
        <h1 id="main-header">ShipStack</h1>
        <div class="main-box">
            <div class="origin-box card">
                <h2>Enter your store location:</h2>
                <input
                    class="input-text"
                    v-model="clusterData.origin"
                    type="text"
                    placeholder="Enter address"
                />
            </div>
            
            <DestinationsCard />
        </div>

        <div class="clusters-grid">
            <ClusterCard
                v-for="c in clusterData.clusters"
                :key="c.groupName"
                :locations="c.locations"
                :clusterNumber="c.groupName"
            />
        </div>

        <div class="button-container">
            <button class="btn-cluster" @click="downloadAsExcel()">
                Download as Excel
            </button>
        </div>
    </div>
</template>

<style scoped>
.form-container {
    max-width: 800px;
    margin: 0 auto;
}

.button-container {
    display: flex;
    justify-content: center;
    margin: 2rem 0;
}

.clusters-grid {
    display: grid;
    gap: 1rem;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    margin: 2rem 0;
}

@media (max-width: 640px) {
    .clusters-grid {
        grid-template-columns: 1fr;
    }
}
</style>