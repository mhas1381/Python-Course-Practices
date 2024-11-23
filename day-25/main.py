# with open('weather-data.csv') as input_csv:
#     data = input_csv.readlines()
#
# print(data)

# import csv
#
# with open('weather-data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv('weather-data.csv')
# temp_list = data['temp'].to_list()
# print(data['temp'].mean())
# print(data['temp'].max())
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.temp * 9/5 + 32)


# data_dict = {
#     'students':['ali' , 'mamad' , 'sepehr'],
#     'grades': [15 , 10 , 19]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')

# data = pandas.read_csv('2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')
# gray_count = data[data['Primary Fur Color'] == "Gray"].__len__()
# cinnamon_count = data[data['Primary Fur Color'] == "Cinnamon"].__len__()
# black_count = data[data['Primary Fur Color'] == "Black"].__len__()
#
# data_dict = {
#     'Primary Fur Color':["Gray" , "Cinnamon" , "Black"],
#     'Count':[gray_count , cinnamon_count , black_count]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv('colors_count.csv')
