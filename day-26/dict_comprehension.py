sentence = "What is the Airspeed Velocity of an Unladan Swallow"

words = list(sentence.split(" "))

# result = {word:len(word) for word in words}
# print(result)

weather_c ={
    "Sunday" : 23,
    "Monday" : 12,
    "Tuesday" : 15
}

weather_f = {day:(temp_c * 9/5)+32 for (day,temp_c) in weather_c.items() }
print(weather_f)