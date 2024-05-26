import boto3

def associate_route_table(route_table_id, subnet_id):
    ec2 = boto3.client('ec2')
    ec2.associate_route_table(RouteTableId=route_table_id, SubnetId=subnet_id)
    print(f'Associated Route Table {route_table_id} with Subnet {subnet_id}')

private_route_table_id= "rtb-007108d93d97374a1"  # Replace with the actual ID
private_subnet_id= "subnet-0d39cc69c01270494"    # Replace with the actual ID
associate_route_table(private_route_table_id, private_subnet_id)