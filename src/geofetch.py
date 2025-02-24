from src.handlers.api_handler import GeoAPIHandler
from src.config.api_config import GeoAPIConfig
from src.utils.validate_util import validate_input

class GeoFetch:
    """
    A class to fetch geographical data for a list of locations.

    This class initializes the API configuration and handler, and provides a method
    to fetch geographical data for a list of input locations.

    This class makes this package modular and allows for easy extension of functionality.
    Other projects just import this class and use the fetch_data method to get geographical data.

    Attributes:
        config (GeoAPIConfig): The API configuration object.
        api_handler (GeoAPIHandler): The API handler object.
    """

    def __init__(self):
        """
        Initializes the GeoFetch object with API configuration and handler.
        """
        self.config = GeoAPIConfig()
        self.api_handler = GeoAPIHandler(self.config)

    def fetch_data(self, input_list):
        """
        Fetches geographical data for a list of input locations.

        This method validates each input location, determines the appropriate API endpoint,
        and fetches the geographical data using the API handler.

        Args:
            input_list (list): A list of location strings to fetch data for.

        Returns:
            list: A list of dictionaries containing the geographical data for each location.
        """
        results = []
        for input_str in input_list:
            input_str = validate_input(input_str)
            endpoint = "zip" if len(input_str) == 5 and input_str.isdigit() else "direct"
            response = self.api_handler.get_data(endpoint, input_str)
            results.append(response)

        return results