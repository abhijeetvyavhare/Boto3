import boto3

# Create IAM client
iam = boto3.client('iam')

def detach_policy_from_role():
    role_name = input("Enter the role name to detach policy: ")
    policy_arn = input("Enter the policy ARN to detach: ")
    try:
        iam.detach_role_policy(RoleName=role_name, PolicyArn=policy_arn)
        print(f"Policy {policy_arn} detached from role {role_name}.")
    except Exception as e:
        print(f"Error detaching policy {policy_arn} from role {role_name}: {e}")

# Run the function
detach_policy_from_role()
