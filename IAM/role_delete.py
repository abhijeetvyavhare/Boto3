import boto3

# Create IAM client
iam = boto3.client('iam')

def delete_role():
    role_name = input("Enter the role name to delete: ")
    try:
        iam.delete_role(RoleName=role_name)
        print(f"Role {role_name} deleted.")
    except Exception as e:
        print(f"Error deleting role {role_name}: {e}")

# Run the function
delete_role()
