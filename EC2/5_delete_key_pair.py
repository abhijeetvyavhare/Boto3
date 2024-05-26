import boto3

ec2 = boto3.client('ec2')

def delete_key_pair(key_name):
    try:
        ec2.delete_key_pair(KeyName=key_name)
        print(f"Key Pair Deleted: {key_name}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    key_name = input("Enter key pair name: ")
    delete_key_pair(key_name)
