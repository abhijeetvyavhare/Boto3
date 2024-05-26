import boto3

# Create IAM client
iam = boto3.client('iam')

# List users
response = iam.list_users()

for user in response['Users']:
    print(f"User: {user['UserName']} - Created on {user['CreateDate']}")
