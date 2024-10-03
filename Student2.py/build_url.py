# build_url.py
# How to dynamically build URLs using parameters like the API key.
# Understanding URL structure for API requests.

def build_url(api_key):
    """
    TODO: The 2nd student needs to create a function that builds the NASA API URL.
    Use the API key to dynamically build the URL for the APOD endpoint.
    """
    if not api_key:
        raise ValueError ("API key is required.")
    
    base_url = "https://api.nasa.gov/planetary/apod"
    url = f"{base_url}?api_key={api_key}"
    return url
