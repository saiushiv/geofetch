import requests

def make_request(base_url, endpoint, api_key, input_data):
    url = f"{base_url}{endpoint}"
    
    # Include api key and input_data as query parameters
    if endpoint == "/zip":
        params = {
            "zip": input_data,
            "appid": api_key,
        }
    else:
        params = {
            "q": input_data,
            "appid": api_key,
        }

    # Make the GET request to the API
    response = requests.get(url, params=params)

    # Return the JSON response if successful, else an error message
    if response.status_code == 200:
        response_json = response.json()
        if isinstance(response_json, list) and response_json:  # Ensure it's a non-empty list
            return response_json[0]
        return response_json or {"error": "Invalid input. Empty response received"}  # Handle empty JSON response

    return {"error": f"Request failed with status {response.status_code}"}