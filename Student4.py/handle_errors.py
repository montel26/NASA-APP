# handle_errors.py
# Key learning points for the 4th student:

# Error handling with APIs (e.g., handling HTTP status codes).
# Raising and catching exceptions.
import requests
response = requests.get('https://api.nasa.gov/planetary/apod?api_key=LIpDwAx5jRWNQxpeBWuiD40EPCyfRPuYXtSfIhLz')
print(response.status_code)
def handle_errors(response):
    """
    TODO: The 5th student will handle HTTP errors and validate the API response.
    """
    try:
        response.raise_for_status()  # Raises an exception for bad HTTP codes
        return response.json()
      # Return parsed JSON data if successful
    except Exception as err:
        print(f"Error fetching data: {err}")
        return None
    except requests.exceptions.HTTPError as errh:
        print("An Http Error occurred:" + repr(errh))
        return None
    except requests.exceptions.ConnectionError as errc:
        print("An Error Connecting to the API occurred:" + repr(errc))
        return None
    except requests.exceptions.Timeout as errt:
        print("A Timeout Error occurred:" + repr(errt))
        return None
    except requests.exceptions.RequestException as err:
        print("An Unknown Error occurred" + repr(err))
        return None
print(handle_errors(response))