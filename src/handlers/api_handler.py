from src.utils.request_util import make_request

class GeoAPIHandler:
    """
    A handler class to interact with the Geo API.

    This class provides methods to get data from the API based on the endpoint type and input data.

    Attributes:
        config (GeoAPIConfig): The API configuration object.
    """

    def __init__(self, config):
        """
        Initializes the GeoAPIHandler with the given configuration.

        Args:
            config (GeoAPIConfig): The API configuration object.
        """
        self.config = config

    def get_data(self, endpoint_type, input_data) -> dict:
        """
        Get data from the API based on the endpoint type and input data.

        This method determines the appropriate endpoint URL based on the endpoint type,
        makes the request using the provided input data, and returns the response.

        Args:
            endpoint_type (str): The type of endpoint to use ('zip' or 'direct').
            input_data (str): The input data to include in the query parameters.

        Returns:
            dict: The JSON response from the API.
        """
        
        # Determine the endpoint URL based on the type
        if endpoint_type == "zip":
            endpoint = "/zip"
        else:
            endpoint = "/direct"

        # Make the request and return the response
        response = make_request(self.config.base_url, endpoint, self.config.api_key, input_data)
        return response