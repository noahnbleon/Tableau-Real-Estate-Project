import requests

def get_lat_long(town_name):
    
    # Append 'Connecticut' to the town name for more specific geocoding
    full_query = f"{town_name}, Connecticut"
    
    # Encode the town name to be URL-friendly
    town_name_encoded = requests.utils.quote(full_query)

    # Nominatim API endpoint with the encoded town name
    url = f"https://nominatim.openstreetmap.org/search?q={town_name_encoded}&format=json"

    # Make the request
    response = requests.get(url, headers={"User-Agent": "YourAppName"})

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        if data:
            # Extract latitude and longitude
            latitude = data[0]['lat']
            longitude = data[0]['lon']
            return latitude, longitude
        else:                                                                                                               
            return None, None
    else:
        return None, None       