# handle_errors.py
# Key learning points for the 4th student:

# Error handling with APIs (e.g., handling HTTP status codes).
# Raising and catching exceptions.
def handle_errors(response):
    """
    TODO: The 5th student will handle HTTP errors and validate the API response.
    """
    try:
        response.raise_for_status()  # Raises an exception for bad HTTP codes
        return response.json()  # Return parsed JSON data if successful
    except Exception as err:
        print(f"Error fetching data: {err}")
        return None
