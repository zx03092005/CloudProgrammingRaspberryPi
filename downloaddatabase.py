import boto3
import json
import commands
dynamodb_client = boto3.client('dynamodb')
rds_client = boto3.client('rds')
def download_from_dynamodb() :	
	messages = commands.getoutput("aws dynamodb scan --table-name ttdb-mobilehub-354773299-old-man")
	s = json.loads(messages)
	f=open('dynamodb', 'w')
	for i in s["Items"] :
		print "Date", 	  '\t', i["Date"]['S']
		print "Text", '\t', i["Text"]['S']
		print "Device",   '\t', i["Device"]['S'], '\n'
		f.write(i['Date']['S'])
		f.write('\n')
		f.write(i['Text']['S'])
		f.write('\n')
		f.write(i['Device']['S'])
		f.write('\n')
