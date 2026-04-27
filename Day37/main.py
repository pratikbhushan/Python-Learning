import requests
from datetime import datetime
import os

USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = os.environ.get("GRAPH_ID")

pixela_endpoint = "https://pixe.la/v1/users"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id" : GRAPH_ID,
    "name" : "Cycling graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}




pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now().strftime('%Y%m%d')

pixel_config = {
    "date" : today,
    "quantity" : "9.5",
}



pixel_update_endpoint = f"{pixel_creation_endpoint}/{today}"

pixel_update_config = {
    "quantity" : "6.3"
}

response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
print(response.text)