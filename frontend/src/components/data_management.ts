import { reactive } from "vue";
import axios from "axios";
import * as XLSX from "xlsx";
interface Cluster {
  groupName: string;
  locations: string[];
}

 export const clusterData = reactive({
  origin: "",
  destinations: [] as unknown as [string],
  clusters: [] as unknown as [Cluster],
  newDestination:"",

  async fetchClusters() {
    const jsonData = {
      destinations: this.destinations,
      origin: this.origin,
    };

    try {
      console.log(jsonData);
      const response = await axios.post(
        "http://127.0.0.1:8000/uploadAddr",
        jsonData
      );

      this.clusters = JSON.parse(response.data);
      console.log(this.clusters);
    } catch (error) {
      console.error("Error fetching posts:", error);
    }
  }, //end of fetch clusters

  flatten(data: [Cluster]) {
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
  }, //end of flatten
  downloadAsExcel() {
    const flattenedData = this.flatten(this.clusters as [Cluster]);

    const worksheet = XLSX.utils.json_to_sheet(flattenedData);
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, "Clusters");
    XLSX.writeFile(workbook, "shipping_groups.xlsx");
  }, //end of downloadExcel

  updateClusterCardDestinations(newData: [string]) {
    Object.assign(this.destinations, newData);
  }, //end of updateClusterDest

   addDestinations  (){
    if (this.newDestination) {
      this.destinations.push(this.newDestination);
      this.newDestination = "";
      
    }
  },
   deleteDestination  (index: number){
    this.destinations.splice(index, 1);
  },

});
