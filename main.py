import sys
from src.handlers.api_handler import GeoAPIHandler
from src.config.api_config import GeoAPIConfig
from src.utils.validate_util import validate_input
from src.utils.logger import logger

def main():
    input_list = sys.argv[1:]  # Get the list of strings from locations from CLI arguments

    if not input_list:
        logger.error("Invalid input. Please provide a valid list of location.")
        return
    
    # Load the API configuration
    config = GeoAPIConfig()

    # Initialize the APIHandler with the config
    api_handler = GeoAPIHandler(config)

    for input_str in input_list:
        input_str = validate_input(input_str)  # Verify and clean the input string
        
        # Decide which API to hit based on string length
        if input_str == "invalid":
            continue # Skip to the next input string
        elif len(input_str) == 5:
            endpoint = "zip" # Use the zip code endpoint for 5-character US zip strings
        else:
            endpoint = "direct" # Use the direct endpoint for fetch direct location using city name

        # Call the appropriate API
        response = api_handler.get_data(endpoint, input_str)
        logger.info(f"Response for '{input_str}': {response}")

if __name__ == "__main__":
    main()