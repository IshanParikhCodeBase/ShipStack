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
</script>

<template>
    <div class="cluster-card">
        <div class="cluster-icon">{{ props.clusterNumber == "-1" ? "🚫" : "🚚" }}</div>
        <h2 class="cluster-header">
            {{ props.clusterNumber == "-1" ? "Outlier(s)" : "Group " + props.clusterNumber }}
        </h2>
        <ul class="location-list">
            <li class="location" v-for="l in props.locations" :key="l">
                📍 {{ l }}
            </li>
        </ul>
    </div>
</template>

<style scoped>
.cluster-card {
    background: var(--color-card);
    border: 1px solid var(--color-border);
    border-radius: 8px;
    padding: 1.5rem;
    margin: 1rem 0;
    transition: border-color 0.25s;
    position: relative;
}

.cluster-card:hover {
    border-color: var(--color-accent);
}

.cluster-icon {
    position: absolute;
    top: 1rem;
    right: 1rem;
    font-size: 1.5rem;
    opacity: 0.5;
}

.cluster-header {
    margin-bottom: 1rem;
    color: var(--color-text);
    font-size: 1.25rem;
    font-weight: 600;
}

.location-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.location {
    color: var(--color-text-secondary);
    padding: 0.5rem;
    border-radius: 4px;
    transition: all 0.15s ease-in-out;
}

.location:hover {
    background: var(--color-border);
    color: var(--color-text);
}
</style>