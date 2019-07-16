import json*
import boto3
import sys
import logging
from boto3.dynamodb.conditions import Key, Attr

#creating dynamodb table, if not already create
ami_updated = []

def ami_lookup(list_of_filters):
	ami_latest_list = []
	EC2 = boto3.client('ec2', region_name='us-east-1')
	for filter in list_of_filters:
		response = EC2.describe_images(
			Owners=['309956199498'], 
			Filters=[
			{
			'Name':'name',
			'Values': [filter]
			}
			]
			)
		sorted_list = sorted(response['Images'],
              		key=lambda x: x['CreationDate'],
              		reverse=True)
		ami_latest_list.append(sorted_list[0])
	        
	return ami_latest_list
        
	
def ami_updater(ami_name,ami_id):
	dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
	table = dynamodb.Table('Latestamis')
    	original_item = table.query(
		 KeyConditionExpression=Key('AMI').eq(ami_name)
   	 )
	
#    if original_item['item'] or original_item ['item']['LatestID'] !=  ami['ImageId']: 
	try:
		ami_in_db = original_item['Items'][0]
	except:
		ami_in_db = []
	if ami_in_db == [] or ami_in_db['LatestID'] != ami_id: 
     		if ami_in_db != []:
			response = table.delete_item(
			Key={
  			'AMI': ami_name,
			'LatestID': ami_in_db['LatestID']
         		}
     			)
		response = table.put_item(
	 	Item={
  		'AMI': ami_name,
		'LatestID': ami_id
         	}
     		)
     		updated = True
		ami_updated.append([ami_name,updated])
	else:	
		updated = False
		ami_updated.append([ami_name,updated])
     		print("no need to update")

	return ami_updated
	
		
		
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

filter_list = ['RHEL-6.8_HVM_GA-20*Access*','RHEL-6.9*HVM_GA-20*Access*','RHEL-6.10*HVM_GA-20*Access*','RHEL-7.4*HVM_GA-20*Access*','RHEL-7.5_HVM_GA-20*Access*','RHEL-7.6*HVM_GA-20*Access*']
images_returned = ami_lookup(filter_list)
sns_notification = []
for image in images_returned:
	sns_notification.append(ami_updater(image['Name'],image['ImageId']))
print(sns_notification)

