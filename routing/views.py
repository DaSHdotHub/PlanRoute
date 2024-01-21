import requests
import os
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