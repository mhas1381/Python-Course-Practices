import smtplib
import datetime as dt
from random import choice

my_email = ""
password = ""



today = dt.datetime.now().weekday()


if today == 0:
    with open('quotes.txt') as file:
        quotes = file.readlines()
        quote = choice(quotes)
    print(quote)

    with smtplib.SMTP("smtp.google.com") as connection:
        connection.starttls()
        connection.login(user = my_email , password=password)
        connection.sendmail(from_addr=my_email , to_addrs="test@gmail.com" , msg=random.choice(quotes))
