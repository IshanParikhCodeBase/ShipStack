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
                
                <hr class="separator" />
                
                <div class="radius-container">
                    <div class="radius-label">
                        <h2>Cluster radius</h2>
                        <div class="info-icon" title="Locations father than this distance, become part of two distinct cluster.">
                            ⓘ
                        </div>
                    </div>
                    <input
                        class="input-text"
                        type="text"
                        placeholder="Enter cluster radius"
                        v-model="clusterData.epsilon"
                    />
                </div>
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

.radius-container {
    margin-top: 1rem;
}

.radius-label {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.5rem;
}

.radius-label h2 {
    margin: 0;
}

.info-icon {
    cursor: help;
    color: #646cff;
    font-size: 1.2rem;
    margin-top: 2px;
}

.separator {
    margin: 1.5rem 0;
    border: none;
    border-top: 1px solid rgba(131, 132, 137, 0.2);
}

@media (max-width: 640px) {
    .clusters-grid {
        grid-template-columns: 1fr;
    }
}
</style>