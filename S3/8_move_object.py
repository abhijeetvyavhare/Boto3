import boto3

def move_object():
    s3_client = boto3.client('s3')
    source_bucket_name = input("Enter the name of the source bucket: ")
    source_object_key = input("Enter the key (name) of the source object: ")
    destination_bucket_name = input("Enter the name of the destination bucket: ")
    destination_object_key = input("Enter the key (name) of the destination object: ")
    
    try:
        copy_source = {
            'Bucket': source_bucket_name,
            'Key': source_object_key
        }
        s3_client.copy_object(CopySource=copy_source, Bucket=destination_bucket_name, Key=destination_object_key)
        print(f"Object '{source_object_key}' copied successfully from '{source_bucket_name}' to '{destination_bucket_name}' as '{destination_object_key}'.")

        s3_client.delete_object(Bucket=source_bucket_name, Key=source_object_key)
        print(f"Object '{source_object_key}' deleted successfully from '{source_bucket_name}'.")
    except s3_client.exceptions.NoSuchKey:
        print(f"Object '{source_object_key}' does not exist in '{source_bucket_name}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    move_object()
