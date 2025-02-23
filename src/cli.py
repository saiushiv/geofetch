import sys
from src.geofetch import GeoFetch
from src.utils.validate_util import validate_input
from src.utils.logger import logger

def main():
    """
    Main function to fetch geographical data for a list of locations provided via CLI arguments.
    This class makes this package available as a CLI command.

    This function:
    1. Retrieves the list of location strings from the command-line arguments.
    2. Validates the input list.
    3. Initializes the GeoFetch object.
    4. Fetches geographical data for each location.
    5. Logs the response for each location to CLI.

    Raises:
        ValueError: If no locations are provided as input.
    """
    
    # Get the list of strings of locations from CLI arguments
    input_list = sys.argv[1:]

    if not input_list:
        raise ValueError("Invalid input. Please provide a valid list of locations.")
    
    # Initialize the GeoFetch object
    geo_fetch = GeoFetch()
    results = geo_fetch.fetch_data(input_list)
    
    # Log the response for each location
    for input_str, response in zip(input_list, results):
        logger.info(f"Response for '{input_str}': {response}\n")

if __name__ == "__main__":
    main()