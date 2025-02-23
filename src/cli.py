import sys
from src.geofetch import GeoFetch
from src.utils.validate_util import validate_input
from src.utils.logger import logger

def main():
    # Get the list of strings of locations from CLI arguments
    input_list = sys.argv[1:]

    if not input_list:
        raise ValueError("Invalid input. Please provide a valid list of locations.")
    
    # Initialize the GeoFetch object
    geo_fetch = GeoFetch()
    results = geo_fetch.fetch_data(input_list)
    
    for input_str, response in zip(input_list, results):
        logger.info(f"Response for '{input_str}': {response}\n")

if __name__ == "__main__":
    main()