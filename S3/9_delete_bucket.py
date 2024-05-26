import boto3
from botocore.exceptions import ClientError

def delete_bucket():
    s3_client = boto3.client('s3')
    bucket_name = input("Enter the name of the bucket to delete: ")

    try:
        # List objects in the bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            objects = response['Contents']
            print(f"The bucket '{bucket_name}' is not empty. It contains {len(objects)} objects.")
            user_input = input("Do you want to delete all objects in the bucket before deleting it? (yes/no): ")
            if user_input.lower() == 'yes':
                # Delete all objects in the bucket
                delete_objects(bucket_name, objects)
            else:
                print("Bucket deletion aborted.")
                return

        # Proceed to delete the bucket
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted successfully.")
    except ClientError as e:
        print(f"Error: {e}")

def delete_objects(bucket_name, objects):
    s3_client = boto3.client('s3')
    for obj in objects:
        object_key = obj['Key']
        try:
            s3_client.delete_object(Bucket=bucket_name, Key=object_key)
            print(f"Deleted object '{object_key}' from bucket '{bucket_name}'.")
        except ClientError as e:
            print(f"Error deleting object '{object_key}': {e}")

if __name__ == "__main__":
    delete_bucket()
