from src.utils.logger import logger

def validate_input(input_str: str) -> str:
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