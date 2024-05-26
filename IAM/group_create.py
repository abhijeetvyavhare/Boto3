import boto3

# Create IAM client
iam = boto3.client('iam')

group_name = input("Enter the group name: ")

# Create group
response = iam.create_group(
    GroupName=group_name
)

print(response)
print(f"Group {response['Group']['GroupName']} created.")
