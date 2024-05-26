import boto3

# Create IAM client
iam = boto3.client('iam')

group_name = input("Enter the group name: ")
user_name = input("Enter the username: ")

# Remove user from group
response = iam.remove_user_from_group(
    GroupName=group_name,
    UserName=user_name
)

print(f"User {user_name} removed from group {group_name}.")
