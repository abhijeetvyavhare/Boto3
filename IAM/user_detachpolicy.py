import boto3

# Create IAM client
iam = boto3.client('iam')

user_name = input("Enter the username: ")

# Detach policy from user
response = iam.detach_user_policy(
    UserName=user_name,
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
)

print(f"Policy detached from user.")
