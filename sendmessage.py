import boto3 
sns_client = boto3.client('sns')

def send_email_message() :
	sns_client.publish(
		TopicArn='arn:aws:sns:us-east-1:661664929584:zx03092005_raspberrypi_email', 
		Message='Test Message'
		)

def send_phone_message(mMessage, mPhoneNumber) :
	sns_client.publish(
		PhoneNumber=mPhoneNumber, 
		Message=mMessage
		)
