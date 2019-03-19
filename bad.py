import logging
import os
import sys
import glob
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
		logger.write(line)
	
	#full_log = open(good_file)
	#for line in full_log:
		#if "031931797306" in line:
			#full_log = open(good_file)
			#for log_line in full_log:
				#logger.write(log_line)
logger.close()

try:
session = get_master_credentials(image_account,access_key,secret_key)
        s3 = session.client('s3')
        try:
           bucket = 'aig-image-factory-logs'
           directory_name = "/errorreports"
           path = os.path.join(aws_account_number, timestamp, master_ami_name, directory_name)
           s3.upload_file('errorami.log', bucket, path)
except Exception as e:
         print(e)
         raise(e)
