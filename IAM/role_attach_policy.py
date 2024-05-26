import boto3

# Create IAM client
iam = boto3.client('iam')

def attach_policy_to_role():
    role_name = input("Enter the role name to attach policy: ")
    policy_arn = input("Enter the policy ARN to attach: ")
    try:
        iam.attach_role_policy(RoleName=role_name, PolicyArn=policy_arn)
        print(f"Policy {policy_arn} attached to role {role_name}.")
    except Exception as e:
        print(f"Error attaching policy {policy_arn} to role {role_name}: {e}")

# Run the function
attach_policy_to_role()
