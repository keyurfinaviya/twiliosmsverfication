import os
from twilio.rest import Client


account_sid = "AC4d012a1f4e6fe637206fcb3bcc4c43b6"
auth_token = "3b580097ef1f3b4b42480aa3740af68e"
Client = Client(account_sid, auth_token)


def send_sms(user_code, phone_number):
	message = Client.messages.create(
			body = f'Your verification code is: {user_code}',
			from_ = "+16193893327",
			to = f'{phone_number}'
		) 