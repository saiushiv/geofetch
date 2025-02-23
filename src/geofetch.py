from src.handlers.api_handler import GeoAPIHandler
from src.config.api_config import GeoAPIConfig
from src.utils.validate_util import validate_input

class GeoFetch:
    def __init__(self):
        self.config = GeoAPIConfig()
        self.api_handler = GeoAPIHandler(self.config)

    def fetch_data(self, input_list):
        results = []
        for input_str in input_list:
            input_str = validate_input(input_str)
            endpoint = "zip" if len(input_str) == 5 and input_str.isdigit() else "direct"
            response = self.api_handler.get_data(endpoint, input_str)
            results.append(response)

        return results