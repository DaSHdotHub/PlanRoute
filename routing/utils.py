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
    if depart_at is None:
        depart_at = datetime.now().replace(hour=13, minute=0, second=0, microsecond=0)  # 1 PM

    url = f"https://api.tomtom.com/routing/1/calculateRoute/{from_address.latitude},{from_address.longitude}:{to_address.latitude},{to_address.longitude}/json?routeType=fastest&avoid=tollRoads,unpavedRoads,ferries&travelMode={travel_mode}&departAt={depart_at.isoformat()}&key={os.environ.get('API_KEY')}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Extract distance from the response and return
        distance = data['routes'][0]['summary']['lengthInMeters'] / 1000  # Convert meters to kilometers
        return distance
    else:
        # Handle error or no result case
        return None
    
def create_and_calculate_address_pairs():
    addresses = list(Address.objects.all())
    for from_address, to_address in permutations(addresses, 2):
        # Avoid duplicating the distance calculation
        if not Distance.objects.filter(from_address=from_address, to_address=to_address).exists():
            distance = calculate_route_distance(from_address, to_address)
            Distance.objects.create(from_address=from_address, to_address=to_address, distance_in_km=distance)