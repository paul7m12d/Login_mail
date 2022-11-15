import smtplib,ssl
from datetime import datetime

now = datetime.now()
hour = now.hour
time = ""

if hour >=0 and hour <= 12:
    time = "good morning"
elif hour >=12 and hour <= 16:
    time = "Good afternoon"
else :
    time = "good evening"

my_email = "p1u12kru@gmail.com"
my_password = "cvaddggegqelznlx"
context = ssl.create_default_context()

connection = smtplib.SMTP("smtp.gmail.com", port=587)


connection.starttls(context=context)
connection.login(my_email, my_password)
connection.sendmail(from_addr=my_email, to_addrs="paulkrupakar777@gmail.com", msg=f"subject:Logged in \n\n{time} boss, I'm up and running!")
connection.close()
