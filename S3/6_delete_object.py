import boto3

def delete_object():
    s3_client = boto3.client('s3')
    bucket_name = input("Enter the name of the bucket containing the object: ")
    object_key = input("Enter the key (name) of the object to delete: ")
    
    try:
        s3_client.delete_object(Bucket=bucket_name, Key=object_key)
        print(f"Object '{object_key}' deleted successfully from '{bucket_name}'.")
    except s3_client.exceptions.NoSuchKey:
        print(f"Object '{object_key}' does not exist in '{bucket_name}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    delete_object()
