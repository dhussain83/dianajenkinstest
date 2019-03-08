import logging
import os
import sys
import glob
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='amierrorreport.log',
                    filemode='a')
bad_files = []
good_files = []
all_files = []

logger = open('test.log','w+') 
logger.write('=====================Start=====================\n')
logger.write('List of AMI factory distribution errors\n')

for bad_file in glob.glob("/var/lib/jenkins/workspace/report_generator/*/outputs.log"):


	log = open(bad_file)
	for line in log:
		if "Error:" in line:
			full_log = open(bad_file)
			for log_line in full_log:
				logger.write(log_line)

logger.write('=====================Start=====================\n')
logger.write('List of AMI factory successful distribution:\n')

for good_file in good_files:
	full_log = open(good_file)
	for line in full_log:
        if "003931215966" in line:
		full_log = open(good_file)
		for log_line in full_log:
			logger.write(log_line)


logger.write('=====================End=====================\n')
logger.close()
