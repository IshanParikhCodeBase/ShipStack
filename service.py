from sklearn.cluster import DBSCAN
import numpy as np
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyD-nXo9Iixx2j_AXl6B-89FLImAEpe5K0Y')

def geocode_address(address):
    geocode_result = gmaps.geocode(address)
    if geocode_result:
        lat, lng = geocode_result[0]['geometry']['location']['lat'], geocode_result[0]['geometry']['location']['lng']
        return lat, lng
    else:
        return None
    
origin = "1600 Amphitheatre Parkway, Mountain View, CA 94043, USA"
destinations = ["New York, NY", "Los Angeles, CA", "Chicago, IL", "Houston, TX", "Miami, FL"]

def calculate_distances(origin, destinations):
    # API results
    results = gmaps.distance_matrix(origin, destinations, mode='driving')
    
    # Foramtting results
    distances_wrt_origin = []
    for i, dest in enumerate(destinations):
        info = results["rows"][0]["elements"][i]
        distances_wrt_origin.append({
            'destination': dest,
            'distance_meters': info['distance']['value'],
            'duration_text': info['duration']['text']
        })
    return distances_wrt_origin

distances_wrt_origin = calculate_distances(origin, destinations)
print('dist wrt store loc',distances_wrt_origin)

# print(f"Distance of each destination w.r.t origin is as follows: {distances_wrt_origin}")

# getting distance values from our list
distances = np.array([[d['distance_meters']] for d in distances_wrt_origin])
print('distances',distances)
epsilon = 1e6  # 1,000,000 meters (1000 km radius)
min_samples = 2  # Minimum points to form a cluster

db = DBSCAN(eps=epsilon, min_samples=min_samples, metric='euclidean').fit(distances)
clusters = {}
labels = db.labels_

distance_to_dest_map = {d['distance_meters']: d['destination'] for d in distances_wrt_origin}

for label, distance in zip(labels, distances):
    if label not in clusters:
        clusters[label] = []
    # Use the distance to find the corresponding destination name (destinaiton is the key)
    distance_value = distance[0]
    destination_name = distance_to_dest_map.get(distance_value)
    clusters[label].append(destination_name)

print("Clustered Destinations:")
for cluster_id, destinations in clusters.items():
    if cluster_id == -1:
        print(f"Cluster {cluster_id} (outliers):")
        for destination in destinations:
            print(f"  {destination}")
    else:
        print(f"Cluster {cluster_id}:")
        for destination in destinations:
            print(f"  {destination}")


