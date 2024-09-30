# "backend.py: This file will handle data processing (parsing and displaying 
# "the APOD info) and will call the functions from api.py."

# Backend.py

from Student1.py import get_api_key
from Student2.py import build_url
from Student3.py import fetch_apod_data
from Student4.py import handle_errors
from Student5.py import parse_apod_data
from Student6.py import display_apod_info


def get_nasa_apod_data():
    """
    This function ties together all the tasks to get and process NASA APOD data.
    """
    # Step 1: Get the API key (from student 1)
    api_key = get_api_key()

    # Step 2: Build the URL for NASA API (2 student task)
    url = build_url(api_key)

    # Step 3: Fetch the data (3 student task)
    response = fetch_apod_data(url)

    # Step 4: Handle errors in the response (4 student task
    apod_data = handle_errors(response)

    # Step 5: Parse the data to extract relevant information (2 student task)
    apod_info = parse_apod_data(apod_data)

    return apod_info


def display_nasa_apod_info(apod_info):
    """
    This function displays the NASA APOD data in a readable format.
    It calls the display function from the 6th student's task.
    """
    # Step 6: Display the information (6th student's task)
    display_apod_info(apod_info)




def main():
    """
    The main script that runs the entire process of fetching and displaying
    NASA's Astronomy Picture of the Day (APOD) data.
    """

    # DO NOT TOUCH
    # Fetch and process NASA APOD data
    apod_info = get_nasa_apod_data()

    # Display the fetched data
    if apod_info:
        display_nasa_apod_info(apod_info)


if __name__ == "__main__":
    main()
