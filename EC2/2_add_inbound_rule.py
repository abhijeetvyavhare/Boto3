import boto3

ec2 = boto3.client('ec2')

def add_inbound_rule(group_id, protocol, port, cidr):
    try:
        ec2.authorize_security_group_ingress(
            GroupId=group_id,
            IpPermissions=[
                {
                    'IpProtocol': protocol,
                    'FromPort': port,
                    'ToPort': port,
                    'IpRanges': [{'CidrIp': cidr}]
                }
            ]
        )
        print(f"Ingress Rule Added to Security Group: {group_id}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    group_id = 'sg-086864874d2d2b2af'  # Replace with your security group ID
    protocol = 'tcp'
    port = 22
    cidr = '0.0.0.0/0'  # Replace with the desired CIDR
    add_inbound_rule(group_id, protocol, port, cidr)
