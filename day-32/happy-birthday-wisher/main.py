##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
from random import randint
import smtplib
# 1. Update the birthdays.csv
data = pandas.read_csv('birthdays.csv')
# 2. Check if today matches a birthday in the birthdays.csv
today = dt.date.today()

birthday = data[(data.month == today.month) & (data.day == today.day)]

names = {row['name']:row['email'] for index, row in birthday.iterrows()}

print(names)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if len(names) != 0:
    for name in names:
        random_letter = randint(1, 3)
        with open(f"letter_templates/letter_{random_letter}.txt") as letter:
            content = letter.read()
            letter_with_name = content.replace("[NAME]", name)
        print(letter_with_name)
        # with smtplib.SMTP("smtp.google.com") as connection:
        #     connection.starttls()
        #     connection.login(user = my_email , password=password)
        #     connection.sendmail(from_addr=my_email , to_addrs=names[name] , msg=letter_with_name)
        print(f"Email has sent to {name} with {names[name]}")

# 4. Send the letter generated in step 3 to that person's email address.