import commands as cmd
import os.path

def capture_photo(filename):
	cmd.getstatusoutput('rm '+filename+'.jpg')
	print "start capturing"
	cmd.getstatusoutput('fswebcam '+filename+'.jpg')
	if not os.path.exists(filename+'.jpg'):
		print "an error occurs during capturing"
		exit(1)
	else :
		print "end   capturing"

