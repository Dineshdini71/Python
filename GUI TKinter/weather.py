import requests

API_KEY = "d30ba6fd3a5a0dc0197d2756dc87ad1c"
BASE_URL= "https://api.openweathermap.org/data/2.5/weather"

def weather_city(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                'City': data["name"],
                'Temparture': f"{data["main"]["temp"]}C",
                'Weather': data['weather'][0]['description'].title(),
                'Humidity': f"{data['main']['humidity']}%",
                'Wind Speed': f"{data['wind']['speed']}m/s"
            }
            return weather
        elif response.status_code == 404:
            print("city is not Found")
        else:
            print("An error occurred. Statue Code: ", response.status_code)
    except Exception as ex:
        print('Error Exception as ', ex)
    return None

def display_weather(weather):
    print("\n------ WEATHER INFORMATION ------")
    for key,value in weather.items():
        print(f"{key}: {value}")

# main Loop
while True:
    print("\n------ WEATHER APP ------")
    city = input("Enter a city (or 'q' for quite): ").strip()
    if city.lower() == 'q':
        break
    weather = weather_city(city)
    if weather:
        display_weather(weather)




















#
# respone = requests.get(url)
#
# if respone.status_code == 200:
#     weather_data = respone.json()
#     print('Success !!', respone.status_code)
#     print(weather_data)
# else:
#     print('Error the Statue Code:', respone.status_code)