import boto3
import requests
from botocore.exceptions import ClientError

def upload_file_from_url():
    s3_client = boto3.client('s3')
    bucket_name = input("Enter the name of the bucket to upload to: ")
    file_url = input("Enter the URL of the file you want to upload: ")
    object_key = input("Enter the key (name) for the object in the bucket: ")
    
    try:
        # Download the file from the URL
        response = requests.get(file_url, stream=True)
        response.raise_for_status()
        
        # Upload the file to S3
        s3_client.upload_fileobj(response.raw, bucket_name, object_key)
        print(f"File '{object_key}' uploaded successfully to '{bucket_name}'.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download the file: {e}")
    except ClientError as e:
        print(f"Failed to upload the file to S3: {e}")

if __name__ == "__main__":
    upload_file_from_url()
