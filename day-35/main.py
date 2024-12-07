import requests

# https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
parameters = {
    "lat":35.7219,
    "lon":51.3347,
    "appid":"8df8f3ff9b94d86a5a03e835e0a650ab",
    "exclude": "minutely,daily,current"
}
response = requests.get(url = "https://api.openweathermap.org/data/3.0/onecall" , params=parameters)
response.raise_for_status()
data = response.json()

weather_slice = data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("bring an umbrella")


