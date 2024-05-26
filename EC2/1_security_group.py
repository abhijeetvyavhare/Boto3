import boto3

ec2 = boto3.client('ec2')

def create_security_group(group_name, description, vpc_id):
    try:
        response = ec2.create_security_group(
            GroupName=group_name,
            Description=description,
            VpcId=vpc_id
        )
        print(f"Security Group Created: {response['GroupId']}")
        return response['GroupId']
    except Exception as e:
        print(e)

if __name__ == "__main__":

    group_name = input("Enter security group name: ")
    description = input("Enter security group description: ")
    vpc_id = input("Enter vpc id: ")
    create_security_group(group_name, description, vpc_id)
