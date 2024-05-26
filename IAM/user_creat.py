import boto3

# Create IAM client
iam = boto3.client('iam')

username = input("Enter User name: ")
# Create user
response = iam.create_user(
    UserName=username
)

print(f"User {response['User']['UserName']} created.")
