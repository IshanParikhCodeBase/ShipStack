import { reactive } from "vue";

export interface Cluster {
  groupName: string;
  locations: string[];
}

 export const clusterData = reactive({
  origin: "",
  epsilon: "",
  destinations: [] as unknown as [string],
  clusters: [] as unknown as [Cluster],
  newDestination:""


});
