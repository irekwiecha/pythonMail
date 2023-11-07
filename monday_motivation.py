import datetime as dt
import random
import smtplib
from priv import email, app_pass  # sensitive data

my_email = email
email_to = "recipent@email.here"
smtp_address = "smtp.gmail.com"  # specify the smtp address of your mail server
day_of_the_week = dt.datetime.now().weekday()
hour = dt.datetime.now().hour
subject = "Monday Motivation"

if day_of_the_week == 0 and 6 <= hour <= 11:
    with open("quotes.txt", mode="r") as f:
        quote = random.choice(f.readlines())
    with smtplib.SMTP(smtp_address) as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_pass)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email_to,
                            msg=f"Subject:{subject}\n\n{quote}")
