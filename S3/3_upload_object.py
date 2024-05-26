import boto3
s3_client = boto3.client('s3')

def upload_file():
    bucket_name = input("Enter the name of the bucket to upload to: ")
    file_path = input("Enter the path to the file you want to upload: ")
    object_key = input("Enter the key (name) for the object in the bucket: ")
    with open(file_path, 'rb') as file:
        s3_client.upload_fileobj(file, bucket_name, object_key)
    print(f"File '{object_key}' uploaded successfully to '{bucket_name}'.")

if __name__ == "__main__":
    upload_file()
