import boto3

def create_and_attach_igw(vpc_id):
    ec2 = boto3.client('ec2')
    igw_response = ec2.create_internet_gateway()
    igw_id = igw_response['InternetGateway']['InternetGatewayId']
    print(f'Created Internet Gateway with ID: {igw_id}')
    
    ec2.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
    print(f'Attached Internet Gateway {igw_id} to VPC {vpc_id}')

vpc_id = 'vpc-04a6fa24147b750ef'  # Replace with the actual VPC ID

create_and_attach_igw(vpc_id)
