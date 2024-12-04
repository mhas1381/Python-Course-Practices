import requests
from datetime import datetime
import smtplib
import time
MY_LAT = 35.689198  # Your latitude
MY_LONG = 51.388973  # Your longitude


def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    x_distance = MY_LAT - iss_latitude
    y_distance = MY_LONG - iss_longitude
    # Your position is within +5 or -5 degrees of the ISS position.

    if -5 <= x_distance <= 5 and -5 <= y_distance <= 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if sunset <time_now < sunrise:
        return True


# def send_email():
#     connection = smtplib.SMTP("smpt.google.com")
#     connection.starttls()
#     connection.login(email = MY_Email , password="password")
#     connection.sendmail(
#         from_addr=MY_Email,
#         to_addrs=MY_Email,
#         msg="Subject:Lookup\n\nThe iss is above you"
#     )

while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        # send_email()
        print("email has sent")
