import boto3
import logging
import os
import sys
import re
import glob

os_flavors = {"156661170251": 0}

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='errorami.log',
                    filemode='a')
bad_files = []
good_files = []
all_files = []

for file in bad_files:
	all_files.remove(file)
	good_files = all_files
	
logger = open('errorami.log','w+') 
logger.write('=====================Start=====================\n')
logger.write('List of AMI factory distribution errors\n')

for bad_file in glob.glob("/var/lib/jenkins/workspace/copy_test/dianabuild/*/output.test"):


	log = open(bad_file)
	for line in log:
		if "071279067022" in line:
			full_log = open(bad_file)
			for log_line in full_log:
				logger.write(log_line)
		elif "156661170251" in line:
			full_log = open(bad_file)
			for log_line in full_log:
				logger.write(log_line)

logger.write('=====================End=====================\n')
logger.write('=====================Start=====================\n')
logger.write('List of AMI factory successful distribution:\n')

for good_file in glob.glob("/var/lib/jenkins/workspace/copy_test/dianabuild/*/output.test"):
	
	for good_file in good_files:
	    full_log = open(good_file)
	    for line in full_log:
	        print(line)
	        match =  re.search("156661170251", log_line)
	        print(match.group())
	        try :
		    flavor_number = os_flavors[match.group()]
		    flavor_number = flavor_number + 1
		    os_flavors[match.group()]= flavor_number
	        except: 
		    os_flavors[match.group()] = 1
		logger.write(log_line)
                logger.write(os_flavors)

		    
logger.close()

#s3 = boto3.client('s3')
#filename = 'errorami.log'
#bucket_name = 'dianahjenkinsaigbucket'
#directory_name = "errorreports"
#path = os.path.join(directory_name,filename)
#s3.upload_file(filename, bucket_name, path)



