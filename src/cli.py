import sys
from src.handlers.api_handler import GeoAPIHandler
from src.config.api_config import GeoAPIConfig
from src.utils.validate_util import validate_input
from src.utils.logger import logger

def main():
    # Get the list of strings of locations from CLI arguments
    input_list = sys.argv[1:]

    if not input_list:
        raise ValueError("Invalid input. Please provide a valid list of locations.")
    
    # Load the API configuration
    config = GeoAPIConfig()

    # Initialize the APIHandler with the config
    api_handler = GeoAPIHandler(config)

    for input_str in input_list:
        # Verify and clean the input string
        input_str = validate_input(input_str)
        
        # Decide which API to hit based on string length
        endpoint = "zip" if len(input_str) == 5 and input_str.isdigit() else "direct"

        # Call the appropriate API
        response = api_handler.get_data(endpoint, input_str)
        logger.info(f"Response for '{input_str}': {response}")

if __name__ == "__main__":
    main()