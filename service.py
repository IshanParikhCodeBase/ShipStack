import googlemaps

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