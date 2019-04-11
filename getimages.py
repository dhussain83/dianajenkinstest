import boto3
from operator import itemgetter

client = boto3.client('ec2')
response = client.describe_images(
    Filters=[
        {
            'Name': 'description',
            'Values': [
                'Amazon Linux AMI*',
            ]
        },
    ],
    Owners=[
        'amazon'
    ]
)
# Sort on Creation date Desc
image_details = sorted(response['Images'],key=itemgetter('CreationDate'),reverse=True)
ami_id = image_details[0]['ImageId']