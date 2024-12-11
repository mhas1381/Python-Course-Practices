import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
Application_ID = os.getenv("Application_ID")
Api_Key = os.getenv("Api_Key")

WEIGHT_KG = 90
HEIGHT_CM = 179
AGE = 22

SHEET_NAME = "workout"
nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = os.getenv("sheety_endpoint")
Bearer = os.getenv("Bearer")

nutritionix_headers = {
    'x-app-id': Application_ID,
    'x-app-key': Api_Key
}
nutritionix_body = {
    "query": input("Tell me which exercise you did:\n"),
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

sheety_headers = {
    "Authorization": f"Bearer {Bearer}"
}

nutritionix_response = requests.post(url=nutritionix_endpoint, json=nutritionix_body,
                                     headers=nutritionix_headers).json()

today = datetime.now().strftime("%Y/%m/%d")
time = datetime.now().time().strftime("%H:%M:%S")

for exercise in nutritionix_response["exercises"]:
    sheety_body = {
        SHEET_NAME: {
            'date': today,
            'time': time,
            'exercise': exercise['name'],
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }}
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_body, headers=sheety_headers)

print(sheety_response.json())
