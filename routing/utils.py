import requests
import os
from datetime import datetime
from itertools import permutations
from core.models import Address, Distance
if os.path.isfile('env.py'):
    import env
    
def update_coordinates(address_instance):
    # Constructing the API request based on TOMTOM API documentation
    address_query = f"{address_instance.street} {address_instance.street_number}, {address_instance.zip_code} {address_instance.city}, {address_instance.country}"
    url = f"https://api.tomtom.com/search/2/geocode/{address_query}.json?key={os.environ.get('API_KEY')}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Extract latitude and longitude from response and update the address instance
        latitude = data['results'][0]['position']['lat']
        longitude = data['results'][0]['position']['lon']
        address_instance.latitude = latitude
        address_instance.longitude = longitude
        address_instance.save()
    else:
        # Handle error or no result case
        pass
    
def calculate_route_distance(from_address, to_address, travel_mode='car', depart_at=None):
    try:
        if depart_at is None:
            depart_at = datetime.now().replace(hour=13, minute=0, second=0, microsecond=0)

        url = f"https://api.tomtom.com/routing/1/calculateRoute/{from_address.latitude},{from_address.longitude}:{to_address.latitude},{to_address.longitude}/json?routeType=fastest&avoid=tollRoads&avoid=unpavedRoads&avoid=ferries&travelMode={travel_mode}&departAt={depart_at.isoformat()}&key={os.environ.get('API_KEY')}"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            distance = data['routes'][0]['summary']['lengthInMeters'] / 1000
            return distance
        else:
            print("Failed to get a valid response from the API:", response.status_code, response.text)
            return None
    except Exception as e:
        print("An error occurred while calculating the route distance:", e)
        return None
    
def create_address_pairs():
    addresses = list(Address.objects.all())
    for from_address, to_address in permutations(addresses, 2):
        if from_address != to_address and not Distance.objects.filter(from_address=from_address, to_address=to_address).exists():
            Distance.objects.create(from_address=from_address, to_address=to_address)

def identify_missing_distances():
    missing_distances = Distance.objects.filter(distance_in_km__isnull=True)
    for distance_obj in missing_distances:
        calculated_distance = calculate_route_distance(distance_obj.from_address, distance_obj.to_address)
        if calculated_distance is not None:
            distance_obj.distance_in_km = calculated_distance
            distance_obj.save()
        else:
            print("Failed to calculate distance for:", distance_obj)