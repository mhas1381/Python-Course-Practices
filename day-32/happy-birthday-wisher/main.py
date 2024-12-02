##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
from random import randint
import smtplib


my_email = "test_email"
password = "password"

def send_email(to_email , subject , body):
    try:
        with smtplib.SMTP("smtp.google.com") as connection:
            connection.starttls()
            connection.login(user = my_email , password=password)
            message = f"Subject: {subject}\n\n{body}"
            connection.sendmail(from_addr=my_email , to_addrs=to_email, msg=message)
            print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {e}")


def check_birthday_and_send_email():
    try:

        data = pd.read_csv('birthdays.csv')
    except FileNotFoundError:
        print("Error: birthdays.csv not found!")
        return


    today = dt.date.today()


    today_birthday = data[(data['month'] == today.month) & (data['day'] == today.day)]
    if today_birthday.empty:
        print("No Birthdays Today!")
        return


    for _, row in today_birthday.iterrows():
        name = row['name']
        email = row['email']
        try:

            random_letter = randint(1, 3)
            with open(f"letter_templates/letter_{random_letter}.txt") as letter:
                content = letter.read()
                letter_with_name = content.replace("[NAME]", name)


            send_email(to_email=email, subject="Happy Birthday!", body=letter_with_name)
        except FileNotFoundError:
            print(f"Error: Letter template {random_letter} not found!")
            continue
if __name__ == "__main__":
    check_birthday_and_send_email()