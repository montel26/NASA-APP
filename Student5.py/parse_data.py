# parse_data.py
# Key learning points for Itu:

# Parsing JSON data and extracting key information.
# Structuring the response data in a readable format.

def parse_apod_data(data):
    """
    TODO: Itu will extract important fields from the APOD data.
    Extract title, explanation, and the media type.
    """
    if data:
        apod_info = {
            "title": data.get("title"),
            "explanation": data.get("explanation"),
            "url": data.get("url"),
            "media_type": data.get("media_type")
        }
        return apod_info
    else:
        print("No data available.")
        return None
