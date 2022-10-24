import smtplib
import os
from email.mime.text import MIMEText
import settings


def send_email():
    message = input("Введите ваше сообщение: ")
    topic = input("Введите тему письма: ")
    sender = settings.EMAIL
    reciver = settings.RECIVERS
    password = settings.PASSWORD
    server = smtplib.SMTP("smtp.{0}".format(settings.DOMAIN), settings.PORT)
    server.starttls()
    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = topic
        recivers = reciver.split(',')
        recivers.pop()
        for rec in recivers:
            server.sendmail(sender, rec, msg.as_string())
            print("The message was sent successfully!")
    except Exception as err:
        print("{0}\nCheck your login or password please!".format(err))


send_email()