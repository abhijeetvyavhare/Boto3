import boto3

def create_route_table_and_route(vpc_id, igw_id):
    ec2 = boto3.client('ec2')
    route_table_response = ec2.create_route_table(VpcId=vpc_id)
    route_table_id = route_table_response['RouteTable']['RouteTableId']
    print(f'Created Route Table with ID: {route_table_id}')
    
    ec2.create_route(
        RouteTableId=route_table_id, 
        DestinationCidrBlock='0.0.0.0/0', 
        GatewayId=igw_id
    )
    print(f'Created route to Internet Gateway {igw_id} in Route Table {route_table_id}')

# Create a route table for the public subnet and add a route to the Internet Gateway
vpc_id= "vpc-08fe235351ba07a7a" # Replace with the actual VPC ID
igw_id= "igw-04143c61550ef0b63" # Replace with the actual IGW ID
create_route_table_and_route(vpc_id, igw_id)