import boto3
s3_client = boto3.client('s3')

def list_buckets():
    response = s3_client.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    print("List of buckets:")
    for bucket in buckets:
        print(bucket)

if __name__ == "__main__":
    list_buckets()
