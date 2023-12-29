
import os
from twilio.rest import Client
import get_numbers

account_sid = ""
auth_token = ""
sid = ""
twilio_number = ""
client = Client(account_sid, auth_token)

get_numbers.import_numbers()

f = open("../phonenumbers.txt", "r")
phone_number_list = f.read().split(',')
print(phone_number_list)


def send_notifs():
    for phone_number in phone_number_list:
        message = client.messages.create(
          body="message content",
          from_=twilio_number,
          #messaging_service_sid=sid,
          to=phone_number
        )
    print('notifications sent!')


if input("are you sure you want to send notifs?(yes/no)") == "yes":
    send_notifs()
else:
    print("notifications not sent")


