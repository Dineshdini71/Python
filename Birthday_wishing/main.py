import pandas as pd
import smtplib as st
from datetime import  datetime
import random

my_mail = "awsdineshdini@gmail.com"
password = "yaryhvypbbrusegs"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
# {new_key:new_value for (key, value) in dict.items()} dictionary comprehensive
birthday_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter{random.randint(1,6)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])
    with st.SMTP("smtp.gmail.com") as connect:
        connect.starttls()
        connect.login(user=my_mail, password=password)
        connect.sendmail(
            from_addr=my_mail,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Birthday Wishes to {birthday_person["name"]}\n\n{content}"
        )
print("Email Sent Successfully 😊 ")