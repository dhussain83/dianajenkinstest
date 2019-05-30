import json
import boto3
import sys
import logging
import difflib

#creating dynamodb table, if not already create

dynamodb_client = boto3.client('dynamodb', region_name='us-east-1')
table_name = 'Latestamis'
existing_tables = dynamodb_client.list_tables()['TableNames']

if table_name not in existing_tables:
    response = dynamodb_client.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'AMI',
                'AttributeType': 'S',
            },
            {
                'AttributeName': 'LatestID',
                'AttributeType': 'S',
            },
        ],
        KeySchema=[
            {
                'AttributeName': 'AMI',
                'KeyType': 'HASH',
            },
            {
                'AttributeName': 'LatestID',
                'KeyType': 'RANGE',
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5,
        },
        TableName=table_name,
    )

table = dynamodb.Table('Latestamis')

table = dynamodb.Table('Latestamis')

table.put_item(
   Item={
        'username': 'ruanb',
        'first_name': ImageId'',
    }
)


#logger = open('testami.log','w+')

#checking RHEL 6.8 ami id
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
print(amis[0]['ImageId'])
#logger.write(amis[0]['ImageId'])
#logger.write("\n")


#checking RHEL 6.9 ami id
response = EC2.describe_images(
Owners=['309956199498'], # RHEL6.9
Filters=[
  {'Name': 'name', 'Values': ['RHEL-6.9*HVM_GA-20*Access*']},
  ],
)
amis = sorted(response['Images'],
              key=lambda x: x['CreationDate'],
              reverse=True)
print(amis[0]['ImageId'])
#logger.write(amis[0]['ImageId'])
#logger.write("\n")


#checking RHEL 6.10 ami id
response = EC2.describe_images(
Owners=['309956199498'], # RHEL6.10
Filters=[
  {'Name': 'name', 'Values': ['RHEL-6.10*HVM_GA-20*Access*']},
  ],
)
amis = sorted(response['Images'],
              key=lambda x: x['CreationDate'],
              reverse=True)
print(amis[0]['ImageId'])
#logger.write(amis[0]['ImageId'])
#logger.write("\n")


#checking RHEL 7.4 ami id
response = EC2.describe_images(
Owners=['309956199498'], # RHEL7.4
Filters=[
  {'Name': 'name', 'Values': ['RHEL-7.4*HVM_GA-20*Access*']},
  ],
)
amis = sorted(response['Images'],
              key=lambda x: x['CreationDate'],
              reverse=True)
print(amis[0]['ImageId'])
#logger.write(amis[0]['ImageId'])
#logger.write("\n")

#checking RHEL 7.5 ami id
response = EC2.describe_images(
Owners=['309956199498'], # RHEL7.5
Filters=[
  {'Name': 'name', 'Values': ['RHEL-7.5_HVM_GA-20*Access*']},
  ],
)
amis = sorted(response['Images'],
              key=lambda x: x['CreationDate'],
              reverse=True)
print(amis[0]['ImageId'])
#logger.write(amis[0]['ImageId'])
#logger.write("\n")

#checking RHEL 7.6 ami id
response = EC2.describe_images(
Owners=['309956199498'], # RHEL7.6
Filters=[
  {'Name': 'name', 'Values': ['RHEL-7.6*HVM_GA-20*Access*']},
  ],
)
amis = sorted(response['Images'],
              key=lambda x: x['CreationDate'],
              reverse=True)
print(amis[0]['ImageId'])
#logger.write(amis[0]['ImageId'])
#logger.close()


#ile1=open("testami.log","r")
#file2=open("previousamilist/default/testami.log","r")
#for line1 in file1:
#        for line2 in file2:
#                if line1==line2:
#                        print("No update found for this ami id\n")
#                else:
#                        #send_SNS notification
#                        print("Updated ami id found. Sending sns notification...")
#                break
#file1.close()
#file2.close()
