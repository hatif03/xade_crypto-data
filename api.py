import requests
from requests.exceptions import RequestException

def call_api(url, params=None, headers=None, timeout=20):
    try:
        # Make a GET request to the API
        response = requests.get(url, params=params, headers=headers, timeout=timeout)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse and return the JSON response
            return response.json()
        else:
            # Print an error message if the request was not successful
            print(f"Error: {response.status_code} - {response.text}")
            return None

    except RequestException as e:
        # Handle exceptions (e.g., timeout, connection error)
        print(f"Error: {e}")
        return None

# Example usage
# api_url = "https://api.example.com/data"
# api_params = {"param1": "value1", "param2": "value2"}
# api_headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
#
# result = call_api(api_url, params=api_params, headers=api_headers)
#
# if result:
#     # Process the API response
#     print(result)
# else:
#     # Handle the case where the API call was not successful
#     print("Failed to retrieve data from the API.")
