import requests
from datetime import datetime
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# datas = response.json()
# longitude = datas["iss_position"]["longitude"]
# latitude = datas["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)
my_lat = 13.604880
my_lng = 79.452027

parameters ={
    "lat": my_lat,
    "lng": my_lng,
    "formatted":0
}



response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()["results"]
print(data)
sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["sunset"].split("T")[1].split(":")[0])
print(type(sunrise))
print(sunset)
# print(sunrise.split("T")[1].split(":")[0])

time_now = datetime.now()
print(time_now.hour)
