import boto3

def upload_image_to_s3(filename) :
	print "start uploading"
	s3_client=boto3.client('s3')
	s3_client.upload_file(filename+'.jpg', 'nthu-103062101', 'final/'+filename+'_remote.jpg')
	print "upload success"