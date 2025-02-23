import os

class GeoAPIConfig:
    def __init__(self):
        self.base_url = "http://api.openweathermap.org/geo/1.0"
        self.api_key = os.getenv("API_KEY")  # Retrieve API key from environment variable
        
        if not self.api_key:
            raise ValueError("API Key not found. Please set it as an environment variable before executing the program.")