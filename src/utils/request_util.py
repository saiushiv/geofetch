import requests

def make_request(base_url, endpoint, api_key, input_data):
    """
    Makes a GET request to the specified API endpoint with the given parameters.

    This function constructs the URL with the base URL and endpoint, includes the API key and input data
    as query parameters, and makes a GET request to the API. It returns the JSON response if the request
    is successful, or an error message if the request fails.

    Args:
        base_url (str): The base URL of the API.
        endpoint (str): The specific API endpoint to call.
        api_key (str): The API key for authentication.
        input_data (str): The input data to include in the query parameters.

    Returns:
        dict: The JSON response from the API if successful.
        dict: An error message if the request fails or the response is empty.
    """
    
    # Construct the URL with the base URL and endpoint
    url = f"{base_url}{endpoint}"
    
    # Include api key and input_data as query parameters and create params as per the endpoint.
    if endpoint == "/zip":
        params = {
            "zip": input_data,
            "limit": 1,
            "appid": api_key,
        }
    else:
        params = {
            "q": input_data,
            "limit": 1,
            "appid": api_key,
        }

    # Make the GET request to the API
    response = requests.get(url, params=params)

    # Return the JSON response if successful, else an error message
    if response.status_code == 200:
        return response.json() or {"error": "Invalid input. Empty response received"}
    else:     
        return {"error": f"Request failed with status {response.status_code}"}