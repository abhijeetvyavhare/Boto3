import boto3

def create_route_table(vpc_id):
    ec2 = boto3.client('ec2')
    route_table_response = ec2.create_route_table(VpcId=vpc_id)
    route_table_id = route_table_response['RouteTable']['RouteTableId']
    print(f'Created Route Table with ID: {route_table_id}')

# Create a route table for the private subnet (no route to IGW)
vpc_id= "vpc-08fe235351ba07a7a"
create_route_table(vpc_id)