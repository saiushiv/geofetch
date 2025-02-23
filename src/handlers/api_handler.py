from src.utils.request_util import make_request

class GeoAPIHandler:
    def __init__(self, config):
        self.config = config

    def get_data(self, endpoint_type, input_data):
        # Determine the endpoint URL based on the type
        if endpoint_type == "zip":
            endpoint = "/zip"
        else:
            endpoint = "/direct"

        # Make the request and return the response
        response = make_request(self.config.base_url, endpoint, self.config.api_key, input_data)
        return response