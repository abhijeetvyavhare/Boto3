import boto3

def list_objects():
    s3_client = boto3.client('s3')
    bucket_name = input("Enter the name of the bucket to list objects from: ")
    response = s3_client.list_objects(Bucket=bucket_name)
    if 'Contents' in response:
        print("List of objects in the bucket:")
        for obj in response['Contents']:
            print(obj['Key'])

if __name__ == "__main__":
    list_objects()
