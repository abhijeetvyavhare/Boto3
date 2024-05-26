import boto3

def create_subnet(vpc_id, cidr_block):
    ec2 = boto3.client('ec2')
    response = ec2.create_subnet(VpcId=vpc_id, CidrBlock=cidr_block)
    subnet_id = response['Subnet']['SubnetId']
    print(f'Created Subnet with ID: {subnet_id}')

vpc_id = 'vpc-04a6fa24147b750ef'  # Replace with the actual VPC ID

# Create two subnets with different CIDR blocks
create_subnet(vpc_id, '10.0.1.0/24')
create_subnet(vpc_id, '10.0.2.0/24')
