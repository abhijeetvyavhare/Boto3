import boto3

ec2 = boto3.client('ec2')

def create_vpc(name):
    response = ec2.create_vpc(CidrBlock='10.0.0.0/16')
    vpc_id = response['Vpc']['VpcId']
    print(f'Created VPC with ID: {vpc_id}')
    
    ec2.create_tags(
        Resources=[vpc_id],
        Tags=[{'Key': 'Name', 'Value': name}]
    )
    print(f'Assigned name "{name}" to VPC {vpc_id}')
    return vpc_id

def create_subnet(vpc_id, cidr_block):
    response = ec2.create_subnet(VpcId=vpc_id, CidrBlock=cidr_block)
    subnet_id = response['Subnet']['SubnetId']
    print(f'Created Subnet with ID: {subnet_id}')
    return subnet_id

def create_and_attach_igw(vpc_id):
    igw_response = ec2.create_internet_gateway()
    igw_id = igw_response['InternetGateway']['InternetGatewayId']
    print(f'Created Internet Gateway with ID: {igw_id}')
    
    ec2.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
    print(f'Attached Internet Gateway {igw_id} to VPC {vpc_id}')
    return igw_id

def create_route_table_and_route(vpc_id, igw_id):
    route_table_response = ec2.create_route_table(VpcId=vpc_id)
    route_table_id = route_table_response['RouteTable']['RouteTableId']
    print(f'Created Route Table with ID: {route_table_id}')
    
    ec2.create_route(
        RouteTableId=route_table_id, 
        DestinationCidrBlock='0.0.0.0/0', 
        GatewayId=igw_id
    )
    print(f'Created route to Internet Gateway {igw_id} in Route Table {route_table_id}')
    return route_table_id

def create_route_table(vpc_id):
    route_table_response = ec2.create_route_table(VpcId=vpc_id)
    route_table_id = route_table_response['RouteTable']['RouteTableId']
    print(f'Created Route Table with ID: {route_table_id}')
    return route_table_id

def associate_route_table(route_table_id, subnet_id):
    ec2.associate_route_table(RouteTableId=route_table_id, SubnetId=subnet_id)
    print(f'Associated Route Table {route_table_id} with Subnet {subnet_id}')

def main():
    # Create a VPC
    vpc_name = "MyVPC"
    vpc_id = create_vpc(vpc_name)

    # Create an Internet Gateway and attach it to the VPC
    igw_id = create_and_attach_igw(vpc_id)

    # Create two subnets (one for public, one for private)
    public_subnet_id = create_subnet(vpc_id, '10.0.1.0/24')
    private_subnet_id = create_subnet(vpc_id, '10.0.2.0/24')

    # Create a route table for the public subnet and add a route to the Internet Gateway
    public_route_table_id = create_route_table_and_route(vpc_id, igw_id)
    associate_route_table(public_route_table_id, public_subnet_id)

    # Create a route table for the private subnet (no route to IGW)
    private_route_table_id = create_route_table(vpc_id)
    associate_route_table(private_route_table_id, private_subnet_id)

if __name__ == "__main__":
    main()
