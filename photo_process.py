from uploadtos3 import upload_image_to_s3
from capture import capture_photo

def photo_process():
	capture_photo('out')
	upload_image_to_s3('out')
