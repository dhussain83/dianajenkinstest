import logging
import os
import sys
import glob
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='errorami.log',
                    filemode='a')
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

logger.close()
