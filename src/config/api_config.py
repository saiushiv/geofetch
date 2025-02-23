import os

class GeoAPIConfig:
    """
    A configuration class for the Geo API.

    This class retrieves the API key from the environment variables and sets the base URL for the API.

    Attributes:
        base_url (str): The base URL of the Geo API.
        api_key (str): The API key for authentication.
    """
    def __init__(self):
        """
        Initializes the GeoAPIConfig object.

        This method retrieves the API key from the environment variable 'GEOFETCH_API_KEY'.
        If the API key is not found, it raises a ValueError.

        Raises:
            ValueError: If the API key is not found in the environment variables.
        """
        self.base_url = "http://api.openweathermap.org/geo/1.0"
        self.api_key = os.getenv("GEOFETCH_API_KEY")  # Retrieve API key from environment variable
        
        if not self.api_key:
            raise ValueError("API Key not found. Please set it as an environment variable before executing the program.")