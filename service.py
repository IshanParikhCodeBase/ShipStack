from sklearn.cluster import DBSCAN
import numpy as np
import googlemaps


# shipping_geocodes = [
#     (40.712776, -74.005974),  # Example: New York City
#     (34.052235, -118.243683), # Example: Los Angeles
# ]

points = [
    (1, 2), (2, 3), (3, 4),  # These are close together
    (10, 11), (11, 12),       # These form another group
    (50, 51)                  # This one may be isolated as noise
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