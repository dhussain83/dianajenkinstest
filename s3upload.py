import boto3

s3 = boto3.client('s3')
filename = 'errorami.log'
bucket_name = 'dianahjenkinsaigbucket'
directory_name = "errorreports"
path = os.path.join(directory_name,filename)
s3.upload_file(filename, bucket_name, path)
