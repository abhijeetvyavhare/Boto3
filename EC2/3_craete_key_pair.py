import boto3

ec2 = boto3.client('ec2')

def create_key_pair(key_name):
    try:
        response = ec2.create_key_pair(KeyName=key_name)
        print(f"Key Pair Created: {response['KeyName']}")
        print(f"Key Material: {response['KeyMaterial']}")
        with open(f"{key_name}.pem", "w") as file:
            file.write(response['KeyMaterial'])
    except Exception as e:
        print(e)

if __name__ == "__main__":
    key_name = input("Enter key pair name: ")
    create_key_pair(key_name)
