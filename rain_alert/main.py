import os
import requests as rq
from twilio.rest import Client
from datetime import datetime

account_sid ="ACb6e7e26f6d4518902cf27adf00688d0a"
auth_token =os.environ.get("AUTH_KEY")
api_key = os.environ.get("OWN_API_KEY")
OWN_END_POINT = "https://api.openweathermap.org/data/2.5/forecast?"

location = {
    "lat": "13.644183",
    "lon": "79.426590",
    "appid": api_key,
    "cnt": 4,
}
# c4fbebf36ae767225d87cb62b367e15f
# d30ba6fd3a5a0dc0197d2756dc87ad1c
response = rq.get(url=OWN_END_POINT, params=location)
# print(response.status_code)
data = response.json()
# print(data["list"][0]["weather"][0]["id"])

now = datetime.now()
current_day = (f"{now.day}-{now.month}-{now.year}")
current_time = (f"{now.hour}:{now.minute}")

will_rain = False
for hour_data in data["list"]:
    print(hour_data)
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            from_="whatsapp:+14155238886",
            body=f"It's going to be raining Today. Remember to bring umbrella ☔. ",
            to="whatsapp:+919573523261",
    )
    print(message.body)