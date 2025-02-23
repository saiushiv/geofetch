from src.utils.logger import logger

def validate_input(input_str: str) -> str:
    """
    Validates and formats the input location string.

    This function trims leading and trailing spaces from the input string, checks if the input
    is a valid US zip code or a city and state combination, and formats it accordingly.

    Args:
        input_str (str): The input location string to validate and format.

    Returns:
        str: The validated and formatted location string.

    Raises:
        ValueError: If the input string is not a valid US zip code or a city and state combination.
    """
    
    input_str = input_str.strip()
    if "," in input_str:
        parts = input_str.split(",")
        if len(parts) == 2:
            return f"{parts[0]},{parts[1]},US"
        else:
            raise ValueError("Invalid City Name. Please provide city name as 'city,state'.")
    elif len(input_str) == 5:
        return input_str
    else:
        raise ValueError("Invalid Location. Please check location. US Zip code should be 5 characters long "
              "and if providing city name, please provide as 'city,state'.")