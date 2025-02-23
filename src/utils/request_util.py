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
        return response_json[0] if isinstance(response_json, list) and response_json else response_json
    return {"error": f"Request failed with status {response.status_code}"}