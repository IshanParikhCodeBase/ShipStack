<script setup lang="ts">
import {clusterData} from '../components/data_management'
import 'primeicons/primeicons.css'
import axios from "axios";
import { ref } from "vue";
const targetColumn = ref("");
import * as XLSX from "xlsx";
const isFileUploaded = ref(false)

const fetchClusters = async () => {
    const jsonData = {
        destinations: clusterData.destinations,
        origin: clusterData.origin,
    };

    try {
        const response = await axios.post(
            "http://127.0.0.1:8000/uploadAddr",
            jsonData
        );
        clusterData.clusters = JSON.parse(response.data);
    } catch (error) {
        console.error("Error fetching posts:", error);
    }
};

const addDestinations = () => {
    if (clusterData.newDestination) {
        clusterData.destinations.push(clusterData.newDestination);
        clusterData.newDestination = "";
    }
};

const deleteDestination = (index: number) => {
    clusterData.destinations.splice(index, 1);
};

const handleFileUpload = (event: Event) => {
  const input = event.target as HTMLInputElement; 
  if (input && input.files) {
    const file = input.files[0];
    console.log(file);
    if (file) {
      isFileUploaded.value = true;
    } else {
      console.warn("No file selected");
      return;
    }

    if (!file.name.endsWith(".xlsx")) {
      alert("Please upload a valid .xlsx file.");
      return;
    }

    // Start reading the file
    const reader = new FileReader();
    reader.onload = (e) => {
      if (e.target?.result) {
        const data = new Uint8Array(e.target.result as ArrayBuffer); // Explicitly cast result to ArrayBuffer
        const workbook = XLSX.read(data, { type: 'array' });

        // Extract data from the first sheet
        const sheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[sheetName];
        const jsonData = XLSX.utils.sheet_to_json(worksheet);

        // Process the extracted data
        // iterating through jsonData to get all the destionations and append them to an array    
        jsonData.forEach((item: any) => clusterData.destinations.push(item.destination))
        
      } else {
        console.error("Failed to read file data.");
      }
    };

    reader.readAsArrayBuffer(file);
  }
};

</script>

<template>
    <div class="destinations-card card">
        <h2>Enter your destinations: 📍</h2>
        <div class="input-group">
            <input
                class="input-text"
                v-model="clusterData.newDestination"
                type="text"
                placeholder="Enter an address"
                @keyup.enter="addDestinations()"
            />
            <button
                @click="addDestinations()"
                class="btn-cluster btn-add"
            >
                <i class="pi pi-plus-circle"></i>
            </button>
            <button class="btn-cluster" @click="fetchClusters()">
                Stack
            </button>
        </div>

        <div class="divider">
            <span>OR</span>
        </div>

        <h2>Upload XLSX 📄</h2>
        <div class="csv-upload">
            <div class="input-group">
                <input
                    class="input-text"
                    type="text"
                    placeholder="Target column name"
                    v-model="targetColumn"
                />
                <label class="btn-cluster btn-upload">
                    <i :class="['pi', isFileUploaded ? 'pi-file-check' : 'pi-upload']"></i>
                    <input
                        type="file"
                        accept=".xlsx"
                        class="hidden"
                        @change="handleFileUpload"
                    />
                </label>
                <button class="btn-cluster" @click="fetchClusters()">
                Stack
                </button>
                
            </div>
        </div>

        <ul class="destinations-list">
            <li v-for="(dest, index) in clusterData.destinations" :key="index" class="destination-item">
                <span>📍 {{ dest }}</span>
                <button
                    @click="deleteDestination(index)"
                    class="btn-cluster btn-delete"
                >
                    <i class="pi pi-trash"></i>
                </button>
            </li>
        </ul>
    </div>
</template>

<style scoped>
.destinations-card {
    margin-top: 1rem;
}

.input-group {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 1rem;
}

.destinations-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.destination-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem;
    margin: 0.5rem 0;
    background: var(--color-input);
    border-radius: 4px;
}

.btn-add {
    color: var(--color-add);
}

.btn-delete {
    color: var(--color-delete);
}

.btn-upload {
    color: var(--color-accent);
}

.btn-add:hover, .btn-delete:hover, .btn-upload:hover {
    border-color: currentColor;
}

.divider {
    display: flex;
    align-items: center;
    text-align: center;
    margin: 1.5rem 0;
}

.divider::before,
.divider::after {
    content: '';
    flex: 1;
    border-bottom: 1px solid var(--color-border);
}

.divider span {
    padding: 0 1rem;
    color: var(--color-text-secondary);
    font-size: 0.875rem;
}

.hidden {
    display: none;
}

.csv-upload {
    margin-top: 1rem;
}
</style>