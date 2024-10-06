import requests
from config import NASA_API_KEY

NASA_ENDPOINT = "https://api.nasa.gov/planetary/earth/assets"


async def fetch_nasa_data(lat: float, lon: float):
    # Fetch real-world environmental data from NASA
    params = {
        "lon": lon,
        "lat": lat,
        "dim": 0.1,
        "api_key": NASA_API_KEY
    }

    response = requests.get(NASA_ENDPOINT, params=params)
    return response.json()
