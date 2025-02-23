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

    # Construct the full URL with query parameters for printing
    request_url = requests.Request('GET', url, params=params).prepare().url
    print(f"Making request to: {request_url}")

    # Make the GET request to the API
    response = requests.get(url, params=params)
    print(response)
    
    # Return the JSON response if successful, else an error message
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status {response.status_code}"}