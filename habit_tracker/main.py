import requests
from datetime import datetime

USERNAME =  "pavi"
TOKEN = "dkjirei23jd45jk2"
GRAPH_ID = "graph1"
pixela_endpoints = "https://pixe.la/v1/users"

user_params ={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoints, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoints}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cyling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoints =f"{pixela_endpoints}/{USERNAME}/graphs/{GRAPH_ID}"


today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometer did you cycle today?"),
}

# response = requests.post(url=pixel_creation_endpoints, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoints}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoints}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
