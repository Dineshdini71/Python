import requests
from datetime import datetime
import smtplib as st
import time

my_mail = "awsdineshdini@gmail.com"
password = "yaryhvypbbrusegs"
MY_LAT = 13.683127 # Your latitude
MY_LONG = 79.352662 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def iss_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and iss_night():
        with st.SMTP("smtp.gmail.com") as connect:
            connect.starttls()
            connect.login(user=my_mail, password=password)
            connect.sendmail(
                to_addrs=dinidinesh71@gmail.com,
                from_addr=my_mail,
                msg="Subject:ISS_Near_For_You LOOK_UP\n\n Hey ISS is above in the SKY."
            )
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



