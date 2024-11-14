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

for label, point in zip(labels, coordinates):
    if label not in clusters:
        clusters[label] = []
    clusters[label].append(point)
print("Clustered Shipping Locations:", clusters)


# Replace 'YOUR_API_KEY' with your actual API key
gmaps = googlemaps.Client(key='YOUR_API_KEY')

def geocode_address(address):
    geocode_result = gmaps.geocode(address)
    if geocode_result:
        lat, lng = geocode_result[0]['geometry']['location']['lat'], geocode_result[0]['geometry']['location']['lng']
        return lat, lng
    else:
        return None

def calculate_distances(origin, destinations):

    results = gmaps.distance_matrix(origin, destinations, mode='driving')
    distances = {}
    for i, row in enumerate(results['rows']):
        distance_text = row['elements'][0]['distance']['text']
        distance_value = int(distance_text.split()[0]) * 1000  # Convert to meters
        distances[destinations[i]] = distance_value
    return distances

# Example usage:
address = "1600 Amphitheatre Parkway, Mountain View, CA 94043, USA"
lat, lng = geocode_address(address)
print(lat, lng)

# Example usage:
origin = "1600 Amphitheatre Parkway, Mountain View, CA 94043, USA"
destinations = ["New York, NY", "Los Angeles, CA", "Chicago, IL"]

distances = calculate_distances(origin, destinations)
for destination, distance in distances.items():
    print(f"Distance to {destination}: {distance} meters")