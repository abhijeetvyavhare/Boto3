import boto3

# Create IAM client
iam = boto3.client('iam')

group_name = input("Enter the group name: ")
user_name = input("Enter the username: ")

# Add user to group
response = iam.add_user_to_group(
    GroupName=group_name,
    UserName=user_name
)

print(f"User {user_name} added to group {group_name}.")
