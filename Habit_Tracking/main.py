import requests
from _datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
# TOKEN = "jhafjkjakgjgsjjgas"
USER = "dini71"
GRAPH_ID = "graph1"

user_param = {
    "token":TOKEN,
    "username":USER,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# r=requests.post(url=pixela_endpoint, json=user_param)
# print(r.text)

graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"
graph_param = {
    "id":GRAPH_ID,
    "name":"walking",
    "unit":"kms",
    "type":"int",
    "color":"ajisai",
}
header = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_param, headers=header)
# print(response.text)
new_graph = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
formatted_time = today.strftime("%Y%m%d")
updated_graph = f"{graph_endpoint}/{GRAPH_ID}/{formatted_time}"
new_graph_param = {
    "date": formatted_time,
    "quantity":input("Enter, How many kilometers walked Today? ")
}

response = requests.post(url=new_graph, json=new_graph_param, headers=header)
print(response.text)

# response = requests.delete(url=up_graph, headers=header)
#
# print(response.text)