# perform all possible s3 operations using python

import boto3

# Initialize the S3 client
s3_client = boto3.client('s3')

def create_bucket():
    bucket_name = input("Enter the name for your S3 bucket: ")
    s3_client.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' created successfully.")

def list_buckets():
    response = s3_client.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    print("List of buckets:")
    for bucket in buckets:
        print(bucket)

def upload_file():
    bucket_name = input("Enter the name of the bucket to upload to: ")
    file_path = input("Enter the path to the file you want to upload: ")
    object_key = input("Enter the key (name) for the object in the bucket: ")
    with open(file_path, 'rb') as file:
        s3_client.upload_fileobj(file, bucket_name, object_key)
    print(f"File '{object_key}' uploaded successfully to '{bucket_name}'.")
   
def list_objects():
    bucket_name = input("Enter the name of the bucket to list objects from: ")
    response = s3_client.list_objects(Bucket=bucket_name)
    if 'Contents' in response:
        print("List of objects in the bucket:")
        for obj in response['Contents']:
            print(obj['Key'])

def delete_bucket():
    bucket_name = input("Enter the name of the bucket to delete: ")
    s3_client.delete_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' deleted successfully.")

def delete_object():
    bucket_name = input("Enter the name of the bucket containing the object: ")
    object_key = input("Enter the key (name) of the object to delete: ")
    
    try:
        # Delete the object
        s3_client.delete_object(Bucket=bucket_name, Key=object_key)
        print(f"Object '{object_key}' deleted successfully from '{bucket_name}'.")
    except s3_client.exceptions.NoSuchKey:
        print(f"Object '{object_key}' does not exist in '{bucket_name}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def copy_object():
    source_bucket_name = input("Enter the name of the source bucket: ")
    source_object_key = input("Enter the key (name) of the source object: ")
    destination_bucket_name = input("Enter the name of the destination bucket: ")
    destination_object_key = input("Enter the key (name) of the destination object: ")
    
    try:
        # Copy the object
        copy_source = {
            'Bucket': source_bucket_name,
            'Key': source_object_key
        }
        s3_client.copy_object(CopySource=copy_source, Bucket=destination_bucket_name, Key=destination_object_key)
        print(f"Object '{source_object_key}' copied successfully from '{source_bucket_name}' to '{destination_bucket_name}' as '{destination_object_key}'.")
    except s3_client.exceptions.NoSuchKey:
        print(f"Object '{source_object_key}' does not exist in '{source_bucket_name}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def move_object():
    source_bucket_name = input("Enter the name of the source bucket: ")
    source_object_key = input("Enter the key (name) of the source object: ")
    destination_bucket_name = input("Enter the name of the destination bucket: ")
    destination_object_key = input("Enter the key (name) of the destination object: ")
    
    try:
        # Copy the object
        copy_source = {
            'Bucket': source_bucket_name,
            'Key': source_object_key
        }
        s3_client.copy_object(CopySource=copy_source, Bucket=destination_bucket_name, Key=destination_object_key)
        print(f"Object '{source_object_key}' copied successfully from '{source_bucket_name}' to '{destination_bucket_name}' as '{destination_object_key}'.")

        # Delete the object from the source bucket
        s3_client.delete_object(Bucket=source_bucket_name, Key=source_object_key)
        print(f"Object '{source_object_key}' deleted successfully from '{source_bucket_name}'.")
    except s3_client.exceptions.NoSuchKey:
        print(f"Object '{source_object_key}' does not exist in '{source_bucket_name}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Menu options
menu_options = {
    "1": create_bucket,
    "2": list_buckets,
    "3": upload_file,
    "4": list_objects,
    "5": delete_bucket,
    "6": delete_object,
    "7": copy_object,
    "8": move_object,   
    "9": exit,

}

# Menu display
while True:
    print("\nMenu:")
    print("1. Create Bucket")
    print("2. List Buckets")
    print("3. Upload File")
    print("4. List Objects in Bucket")
    print("5. Delete Bucket")
    print("6. Delete Object")
    print("7. Copy Object")
    print("8. Move Object")
    print("9. Exit")
    
    choice = input("Enter your choice (1-10): ")
    
    if choice in menu_options:
        menu_options[choice]()
    else:
        print("Invalid choice. Please enter a number between 1 and 10.")
