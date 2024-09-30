# fetch_data.py
import requests
# Key learning points for 3rd:
# Making HTTP requests with requests

# Handling API responses.
def fetch_apod_data(url):
    """
    TODO: The 3rd will implement this function to fetch data from the NASA API.
    Use the 'requests' library to make an HTTP GET request.
    """
    try:
        response = requests.get(url)
        return response
    except Exception as err:
        print(f"An error occurred: {err}")
        return None
