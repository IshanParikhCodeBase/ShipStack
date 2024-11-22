from sklearn.cluster import DBSCAN
import numpy as np
import googlemaps


# shipping_geocodes = [
#     (40.712776, -74.005974),  # Example: New York City
#     (34.052235, -118.243683), # Example: Los Angeles
# ]

points = [
    (1, 2), (2, 3), (3, 4), 
    (10, 11), (11, 12),       
    (50, 51)                  
]

coordinates = np.array(points)

epsilon = 0.1
min_sample = 2

db = DBSCAN(eps=epsilon, min_samples=min_sample, metric='haversine').fit(np.radians(coordinates))

clusters = {}
labels = db.labels_

# for label, point in zip(labels, coordinates):
#     if label not in clusters:
#         clusters[label] = []
#     clusters[label].append(point)
# print("Clustered Shipping Locations:", clusters)


gmaps = googlemaps.Client(key='AIzaSyD-nXo9Iixx2j_AXl6B-89FLImAEpe5K0Y')

def geocode_address(address):
    geocode_result = gmaps.geocode(address)
    if geocode_result:
        lat, lng = geocode_result[0]['geometry']['location']['lat'], geocode_result[0]['geometry']['location']['lng']
        return lat, lng
    else:
        return None

def calculate_distances(origin, destinations):
    # API results
    results = gmaps.distance_matrix(origin, destinations, mode='driving')
    
    # Foramtting results
    distances = {}
    info = results['rows'][0]['elements']
    n = len(info)
    
    for i in range(n):
        distances[destinations[i]] = [info[i]['distance']['value'],info[i]['duration']['text']]

    return distances

# Testing Distance Matrix
origin = "1600 Amphitheatre Parkway, Mountain View, CA 94043, USA"
destinations = ["New York, NY", "Los Angeles, CA", "Chicago, IL"]

distances = calculate_distances(origin, destinations)

print(distances)


# Accessing distances
# key = ['location'] => this will give array of 2 elements
# 0th index = distance
# 1th index = duration