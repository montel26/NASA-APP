# display_data.py
# Key learning points for the 6th student:
# Displaying parsed data in a clean and readable way.
# Understanding how to format and present API data.
import json
import requests

#Extracts specific fields from the data 
# def parse_apod_info(data):
#     parse_info ={
#                 "title":data.get("title"),
#                 "explanation":data.get("explanation"),
#                 "media_type":data.get("media_type"),
#                 "url":data.get("url")
#     }
#     return parse_info

#Retrieve the picture of the day data from NASA API
# def fetch_apod_info(api_key):
#     url ="https://api.nasa.gov/planetary/apod"
#     params = {'api_key': api_key}

#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         return parse_apod_info(response.json())
#     else:
#         print("Error getching data: {response.status_code}")
#         return None
    

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

#Fetch and displays the data when executed
if __name__ == "__main__":
    api_key = "DEMO_KEY"
    apod_info = fetch_apod_info(api_key)
    display_apod_info(apod_info)