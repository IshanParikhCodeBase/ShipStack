This is a shipment aggregator tool, that helps small store owners to group shipment orders
together based on a threshold distance.

User (store owner) is allowed to set the threshold distance.

Distance between every pair of order is calculated, and if the distance is < threshold,
those orders are grouped together in a stack.

The idea is to automate shipment grouping process for a faster and cost-effective deliveries.

Why was DBSCAN utilized, other possible option was to calculate distance between every pair of shipping
locations, however, that would yield a O(n2) time complexity, which we ideally want to avoid.
TBC.