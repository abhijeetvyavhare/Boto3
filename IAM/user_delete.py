import boto3

# Create IAM client
iam = boto3.client('iam')

def delete_user():
    user_name = input("Enter the username to delete: ")
    try:
        response = iam.delete_user(UserName=user_name)
        print(f"User {user_name} deleted.")
    except Exception as e:
        print(f"Error deleting user {user_name}: {e}")

delete_user()
