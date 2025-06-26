from tokenize import blank_re

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dic = data.to_dict()
# print(data_dic)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# avg = sum(temp_list) / len(temp_list)
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get Data in columns
#
# # Below two ways to get the columns
# print(data["condition"])
# print(data.condition)

#Getting Data from a row
# height_temp = data.temp.max()
# print(height_temp)
# print(data[data.day == 'Monday'])
# print(data[data.temp == height_temp])

### Convert celsius to fahrenheit
# monday = data[data.day == 'Monday']
# monday_temp = monday.temp[0]
# monday_temp_F = (monday_temp * 9/5) + 32
# print(monday_temp_F)

# --------------------------------------------------------------------------

# Creating a dataframe from scratch

# data_file= {
#     "student": ['Dinesh', 'Madhu', 'Harsha', 'Balaji'],
#     "score": ['77', '88', '90', '94']
# }
# new_data = pandas.DataFrame(data_file)
# new_data.to_csv('new_file.csv')

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_color_count = len(data[data["Primary Fur Color"] == "Gray"])
red_color_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_color_count)
print(red_color_count)
print(black_color_count)

data_dic = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [grey_color_count, red_color_count, black_color_count]
}

save_data = pandas.DataFrame(data_dic)
save_data.to_csv('Squirrel.csv')















