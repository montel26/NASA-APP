# fetch_data.py
import requests
# Key learning points for 3rd:
# Making HTTP requests with requests

# Handling API responses.
def fetch_apod_data(url):
    success_status_code = 200
    """
    TODO: The 3rd will implement this function to fetch data from the NASA API.
    Use the 'requests' library to make an HTTP GET request.
    """
    try:
        response = requests.get(url)
        if response.status_code == success_status_code:
            return response.json()
        else:
            print(f"error {response.status_code}")
    except requests.exceptions.HTTPError as err:
        print(f"An error occurred: {err}")
        return None
