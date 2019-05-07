import json
import boto3

EC2 = boto3.client('ec2', region_name='us-east-1')
response = EC2.describe_images
Owners=['309956199498'], # RHEL6.8
Filters=[
  {'Name': 'name', 'Values': ['RHEL-6.8_HVM_GA*Access*']},
  ],


amis = sorted(response['Images'],
              key=lambda x: x['CreationDate'],
              reverse=True)
print amis[0]['ImageId']
