import requests
from twilio.rest import Client

STOCK = "Spotify"
COMPANY_NAME = "Spotify Technology S.A"

url = ("https://www.alphavantage.co/query?")
NEWS_URL = ("https://newsapi.org/v2/everything?")

API_KEY = "EYHEAVWHPQ9DQQU2"
NEWS_API_KEY = "a2f9380466914a96bd737f980c45ef1f"


parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":"RELIANCE.BSE",
    "apikey":API_KEY,
}
new_param = {
    "q":COMPANY_NAME,
    "sortBy":"popularity",
    "apiKey":NEWS_API_KEY
}


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").



response = requests.get(url=f"https://www.alphavantage.co/query?", params=parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]  # [new_item for item in data_list] List comprehensive
yesterday =data_list[0]["4. close"]
day_before_yesterday = data_list[1]["4. close"]
difference = float(yesterday) - float(day_before_yesterday)  # This is abs value in python
UP_DOWN = None
if difference > 0:
    UP_DOWN = "🔻"
else:
    UP_DOWN = "🔺"
diff_percent = round((difference / float(yesterday)) * 100)  # calculate the percentage


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if abs(diff_percent) > 0:
    new_respo = requests.get(url=NEWS_URL, params=new_param)
    articles = new_respo.json()["articles"]
    three_articles = articles[:3] # This is Slicing Notation in python, Mainly use to some data in the list like [:2]
    # Headline: {articles.title} \nBrief\n {articel.decription}
    formatted_article = [f"Stock:{STOCK}-{UP_DOWN}{diff_percent}% \n\n HeadLine: {articles["title"]}. \n Brief:{articles["description"]}" for articles in three_articles]
    # STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    account_sid = "ACb6e7e26f6d4518902cf27adf00688d0a"
    auth_token = "c4fbebf36ae767225d87cb62b367e15f"
    client = Client(account_sid, auth_token)
    for article in formatted_article:
        message = client.messages.create(
            body= article,
            from_="+15675220166",
            to="+919573523261",
        )
    print(message.body)
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

