import boto3
import json
import commands 
from photo_process import photo_process 
from sendmessage import send_email_message
from sendmessage import send_phone_message
from downloaddatabase import download_from_dynamodb

try :
	commands.getoutput('rm dynamodb')
	sqs_client = boto3.client('sqs')
	while True :
		messages = commands.getoutput('aws sqs receive-message --queue-url https://sqs.us-east-1.amazonaws.com/661664929584/my-queue --max-number-of-messages 1')
		
		if not messages.startswith('{'):
			print '<waiting for message>'
			continue
		print messages
		j = json.loads(messages)
		
		for i in j["Messages"] :
		 	message = i["Body"]
		 	tokens = message.split("@")
			function_call_flag = 0
			count = 0
			querys = []
		 	for token in tokens :
		 		if token == 'photo' :
		 			function_call_flag = 1
		 			print 'query <photo>'
		 			break
		 		elif token == 'message' :
		 			function_call_flag = 2
		 			print 'query <message>'
		 		elif token == 'database' :
		 			function_call_flag = 3
		 			print 'query database'
		 			break
		 		else :
		 			print count, ' ',token
		 			querys.append(token)
		 			count += 1
		 	if function_call_flag == 0 :			
		 		print 'unexpectd query'
		 		exit(1)
		 	elif function_call_flag == 1 :
		 		photo_process()
		 	elif function_call_flag == 2 :
		 		send_phone_message(querys[0], querys[1])
		 	elif function_call_flag == 3 :
		 		download_from_dynamodb()

			sqs_client.delete_message(
								QueueUrl = "https://sqs.us-east-1.amazonaws.com/661664929584/my-queue",
								ReceiptHandle = i['ReceiptHandle']
								)
		print 'query process success'
		# sqs_client.purge_queue(
		# 						QueueUrl = "https://sqs.us-east-1.amazonaws.com/661664929584/my-queue",
		# 						)
		# break
except KeyboardInterrupt:
	print 'Quit'
	exit(0)