import boto3
import json

# Create IAM client
iam = boto3.client('iam')

def create_user():
    user_name = input("Enter the username to create: ")
    response = iam.create_user(UserName=user_name)
    print(f"User {response['User']['UserName']} created.")

def delete_user():
    user_name = input("Enter the username to delete: ")
    try:
        # Detach all managed policies
        attached_policies = iam.list_attached_user_policies(UserName=user_name)['AttachedPolicies']
        for policy in attached_policies:
            iam.detach_user_policy(UserName=user_name, PolicyArn=policy['PolicyArn'])
            print(f"Detached policy {policy['PolicyName']} from user {user_name}")
        
        # Remove user from all groups
        groups = iam.list_groups_for_user(UserName=user_name)['Groups']
        for group in groups:
            iam.remove_user_from_group(GroupName=group['GroupName'], UserName=user_name)
            print(f"Removed user {user_name} from group {group['GroupName']}")
        
        # Delete the user
        iam.delete_user(UserName=user_name)
        print(f"User {user_name} deleted.")
    except Exception as e:
        print(f"Error deleting user {user_name}: {e}")

def attach_user_policy():
    user_name = input("Enter the username to attach policy: ")
    policy_arn = input("Enter the policy ARN to attach: ")
    iam.attach_user_policy(UserName=user_name, PolicyArn=policy_arn)
    print(f"Policy {policy_arn} attached to user {user_name}.")

def detach_user_policy():
    user_name = input("Enter the username to detach policy: ")
    policy_arn = input("Enter the policy ARN to detach: ")
    iam.detach_user_policy(UserName=user_name, PolicyArn=policy_arn)
    print(f"Policy {policy_arn} detached from user {user_name}.")

def create_group():
    group_name = input("Enter the group name to create: ")
    response = iam.create_group(GroupName=group_name)
    print(f"Group {response['Group']['GroupName']} created.")

def add_user_to_group():
    group_name = input("Enter the group name: ")
    user_name = input("Enter the username to add to the group: ")
    iam.add_user_to_group(GroupName=group_name, UserName=user_name)
    print(f"User {user_name} added to group {group_name}.")

def list_users_in_group():
    group_name = input("Enter the group name: ")
    response = iam.get_group(GroupName=group_name)
    group_name_from_response = response['Group']['GroupName']
    print(f"Users in group {group_name_from_response}:")
    for user in response['Users']:
        print(f"User: {user['UserName']}")

def remove_user_from_group():
    group_name = input("Enter the group name: ")
    user_name = input("Enter the username to remove from the group: ")
    iam.remove_user_from_group(GroupName=group_name, UserName=user_name)
    print(f"User {user_name} removed from group {group_name}.")

def delete_group():
    group_name = input("Enter the group name to delete: ")
    try:
        iam.delete_group(GroupName=group_name)
        print(f"Group {group_name} deleted.")
    except Exception as e:
        print(f"Error deleting group {group_name}: {e}")

def create_role():
    role_name = input("Enter the role name to create: ")
    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "ec2.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }
    response = iam.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(trust_policy)
    )
    print(f"Role {response['Role']['RoleName']} created.")

def attach_role_policy():
    role_name = input("Enter the role name to attach policy: ")
    policy_arn = input("Enter the policy ARN to attach: ")
    iam.attach_role_policy(RoleName=role_name, PolicyArn=policy_arn)
    print(f"Policy {policy_arn} attached to role {role_name}.")

def detach_role_policy():
    role_name = input("Enter the role name to detach policy: ")
    policy_arn = input("Enter the policy ARN to detach: ")
    iam.detach_role_policy(RoleName=role_name, PolicyArn=policy_arn)
    print(f"Policy {policy_arn} detached from role {role_name}.")

def delete_role():
    role_name = input("Enter the role name to delete: ")
    try:
        iam.delete_role(RoleName=role_name)
        print(f"Role {role_name} deleted.")
    except Exception as e:
        print(f"Error deleting role {role_name}: {e}")

def menu():
    while True:
        print("\nIAM Operations Menu")
        print("1. Create User")
        print("2. Delete User")
        print("3. Attach Policy to User")
        print("4. Detach Policy from User")
        print("5. Create Group")
        print("6. Add User to Group")
        print("7. List Users in Group")
        print("8. Remove User from Group")
        print("9. Delete Group")
        print("10. Create Role")
        print("11. Attach Policy to Role")
        print("12. Detach Policy from Role")
        print("13. Delete Role")
        print("14. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_user()
        elif choice == '2':
            delete_user()
        elif choice == '3':
            attach_user_policy()
        elif choice == '4':
            detach_user_policy()
        elif choice == '5':
            create_group()
        elif choice == '6':
            add_user_to_group()
        elif choice == '7':
            list_users_in_group()
        elif choice == '8':
            remove_user_from_group()
        elif choice == '9':
            delete_group()
        elif choice == '10':
            create_role()
        elif choice == '11':
            attach_role_policy()
        elif choice == '12':
            detach_role_policy()
        elif choice == '13':
            delete_role()
        elif choice == '14':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
