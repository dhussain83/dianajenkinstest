import boto3
boto3 = boto3.resource("ec2", region_name="us-east-1")
images = boto3conn.images.filter(Owners=['self']) 
