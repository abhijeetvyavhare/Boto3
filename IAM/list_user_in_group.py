import boto3

# Create IAM client
iam = boto3.client('iam')

group_name = input("Enter the group name: ")

# List users in group
response = iam.get_group(GroupName=group_name)

# Extract the group name from the response
group_name_from_response = response['Group']['GroupName']

for user in response['Users']:
    print(f"User: {user['UserName']} in group {group_name_from_response}")
