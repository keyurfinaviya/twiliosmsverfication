import os
from twilio.rest import Client


account_sid = "AC****************************b6"
auth_token = "3b******************************e"
Client = Client(account_sid, auth_token)


def send_sms(user_code, phone_number):
	message = Client.messages.create(
			body = f'Your verification code is: {user_code}',
			from_ = "+1************",
			to = f'{phone_number}'
		) 