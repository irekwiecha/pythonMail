import datetime as dt
import pandas as pd
import smtplib
from priv import email, app_pass  # sensitive date
from random import randint

my_email = email
smtp_address = "smtp.gmail.com"  # specify the smtp address of your mail server
templates = f"letter_templates/letter_{randint(1, 3)}.txt"
b_days = pd.read_csv("birthdays.csv", usecols=["name", "email", "month", "day"])
month, day = (dt.datetime.now().month, dt.datetime.now().day)  # day and month to check

for index, row in b_days.iterrows():
    if (row["month"], row["day"]) == (month, day):
        with open(templates, mode="r") as f:
            data = f.read()
            letter = data.replace("[NAME]", f"{row['name']}")

        with smtplib.SMTP(smtp_address) as connection:
            connection.starttls()
            connection.login(user=my_email, password=app_pass)
            connection.sendmail(from_addr=my_email,
                                to_addrs=row['email'],
                                msg=f"Subject:Happy B-Day!!!\n\n{letter}")
