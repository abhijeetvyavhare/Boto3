import boto3
import json

# Create IAM client
iam = boto3.client('iam')

# Create role
response = iam.create_role(
    RoleName='MyNewRole',
    AssumeRolePolicyDocument=json.dumps({
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
    })
)

print(f"Role {response['Role']['RoleName']} created.")
