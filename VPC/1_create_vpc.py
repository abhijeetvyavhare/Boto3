import boto3

def create_vpc(name):
    ec2 = boto3.client('ec2')
    # Create the VPC
    response = ec2.create_vpc(CidrBlock='10.0.0.0/16')
    vpc_id = response['Vpc']['VpcId']
    print(f'Created VPC with ID: {vpc_id}')
    
    # Assign a name to the VPC using tags
    ec2.create_tags(
        Resources=[vpc_id],
        Tags=[{'Key': 'Name', 'Value': name}]
    )
    print(f'Assigned name "{name}" to VPC {vpc_id}')


create_vpc("MyVPC")
