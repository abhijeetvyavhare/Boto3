import boto3
from botocore.exceptions import ClientError

def create_bucket():
    s3_client = boto3.client('s3')
    bucket_name = input("Enter the name for your S3 bucket: ")
    
    try:
        # Create the bucket
        response = s3_client.create_bucket(Bucket=bucket_name)
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(f"Bucket '{bucket_name}' created successfully.")
        else:
            print(f"Failed to create bucket '{bucket_name}'.")
        print("Response:", response)
    except ClientError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_bucket()
