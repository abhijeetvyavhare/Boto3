import boto3

# Create IAM client
iam = boto3.client('iam')

group_name = input("Enter the group name: ")

# Delete group
response = iam.delete_group(
    GroupName=group_name
)

print(f"Group {group_name} deleted.")
