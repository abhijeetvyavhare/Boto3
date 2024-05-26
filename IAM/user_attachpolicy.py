import boto3

# Create IAM client
iam = boto3.client('iam')


user_name = input("Enter the username: ")

# Attach policy to user
response = iam.attach_user_policy(
    UserName=user_name,
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
)

print(f"Policy attached to user.")
