import boto3
boto3 = boto3.resource("ec2", region_name="us-east-1")
images = boto3.images.filter(Owners=['self']) 
