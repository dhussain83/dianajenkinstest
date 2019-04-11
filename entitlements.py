import json
import boto3

EC2 = boto3.client('ec2')
response = EC2.describe_images(
    Owners=['679593333241'], # CentOS
    Filters=[
      {'Name': 'name', 'Values': ['CentOS Linux 7 x86_64 HVM EBS *']},
      {'Name': 'architecture', 'Values': ['x86_64']},
      {'Name': 'root-device-type', 'Values': ['ebs']},
    ],
)

amis = sorted(response['Images'],
              key=lambda x: x['CreationDate'],
              reverse=True)
print amis[0]['ImageId']
