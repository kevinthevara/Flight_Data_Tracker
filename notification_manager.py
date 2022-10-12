import requests
from twilio.rest import Client


class NotificationManager:
    def __init__(self):
        self.account_sid = "ACCOUNT_SID"
        self.auth_token = "AUTH_TOKEN"

    def send_message(self, floor):
        for x in floor:
            citycode = x["cityCodeTo"]
            price = x["price"]
            client = Client(self.account_sid, self.auth_token)
            message = client.messages \
                .create(
                to="USER_PHONE_NUMBER",
                from_="TWILIO_PHONE_NUMBER",
                body=f"We found a great deal!  Flight from TOR to {citycode} for onLy ${price}!")
            print(message.status)
