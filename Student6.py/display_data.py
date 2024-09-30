# display_data.py
# Key learning points for the 6th student:

# Displaying parsed data in a clean and readable way.
# Understanding how to format and present API data.

def display_apod_info(info):
    """
    TODO: The 6th student will display the APOD information in a user-friendly format.
    Print the title, explanation, and URL of the APOD content.
    """
    if info:
        print(f"Title: {info['title']}")
        print(f"Explanation: {info['explanation']}")
        print(f"Media Type: {info['media_type']}")
        print(f"URL: {info['url']}")
    else:
        print("No information to display.")
