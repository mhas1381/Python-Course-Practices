import requests
parameters = {
    "lat": 35.689198,
    "lng": 51.388973,
    "formatted" : 0
}

response = requests.get(url='https://api.sunrise-sunset.org/json' ,  params = parameters)
response.raise_for_status()
data = response.json()


print(data)
