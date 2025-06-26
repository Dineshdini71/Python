# with open("weather_data.csv") as data:
#     n = data.readlines()
#     print(n)

# import csv
# temperature = []
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
#####################  P A N D A S  #####################

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])