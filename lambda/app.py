import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = "my-data-bucket"
    s3.put_object(Bucket=bucket_name, Key="output.txt", Body="Hello from Lambda!")
    return {"status": "success"}