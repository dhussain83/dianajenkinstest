import json
import boto3
import sys
import logging
import difflib


logger = open('testami.log','w+')

EC2 = boto3.client('ec2', region_name='us-east-1')
response = EC2.describe_images(
Owners=['309956199498'], # RHEL6.8
Filters=[
  {'Name': 'name', 'Values': ['RHEL-6.8_HVM_GA-20*Access*']},
  ],
)
amis = sorted(response['Images'],
              key=lambda x: x['CreationDate'],
              reverse=True)
logger.write(amis[0]['ImageId'])
logger.write("\n")


EC2 = boto3.client('ec2', region_name='us-east-1')
response = EC2.describe_images(
Owners=['309956199498'], # RHEL6.9
Filters=[
  {'Name': 'name', 'Values': ['RHEL-6.9*HVM_GA-20*Access*']},
  ],
)
amis = sorted(response['Images'],
              key=lambda x: x['CreationDate'],
              reverse=True)
#print(amis[0]['ImageId'])
logger.write(amis[0]['ImageId'])
logger.write("\n")


EC2 = boto3.client('ec2', region_name='us-east-1')
response = EC2.describe_images(
Owners=['309956199498'], # RHEL6.10
Filters=[
  {'Name': 'name', 'Values': ['RHEL-6.10*HVM_GA-20*Access*']},
  ],
)
amis = sorted(response['Images'],
              key=lambda x: x['CreationDate'],
              reverse=True)
#print(amis[0]['ImageId'])
logger.write(amis[0]['ImageId'])
logger.write("\n")


EC2 = boto3.client('ec2', region_name='us-east-1')
response = EC2.describe_images(
Owners=['309956199498'], # RHEL7.4
Filters=[
  {'Name': 'name', 'Values': ['RHEL-7.4*HVM_GA-20*Access*']},
  ],
)
amis = sorted(response['Images'],
              key=lambda x: x['CreationDate'],
              reverse=True)
#print(amis[0]['ImageId'])
logger.write(amis[0]['ImageId'])
logger.write("\n")

EC2 = boto3.client('ec2', region_name='us-east-1')
response = EC2.describe_images(
Owners=['309956199498'], # RHEL7.5
Filters=[
  {'Name': 'name', 'Values': ['RHEL-7.5_HVM_GA-20*Access*']},
  ],
)
amis = sorted(response['Images'],
              key=lambda x: x['CreationDate'],
              reverse=True)
#print(amis[0]['ImageId'])
logger.write(amis[0]['ImageId'])
logger.write("\n")

EC2 = boto3.client('ec2', region_name='us-east-1')
response = EC2.describe_images(
Owners=['309956199498'], # RHEL7.6
Filters=[
  {'Name': 'name', 'Values': ['RHEL-7.6*HVM_GA-20*Access*']},
  ],
)
amis = sorted(response['Images'],
              key=lambda x: x['CreationDate'],
              reverse=True)
#print(amis[0]['ImageId'])
logger.write(amis[0]['ImageId'])
logger.close


file1 = "default/testami.log"
file2 = "previousamilist/testami.log"

diff = difflib.ndiff(open(file1).readlines(),open(file2).readlines())
print ''.join(diff),
