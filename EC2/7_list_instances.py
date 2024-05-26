import boto3

ec2 = boto3.client('ec2')

def describe_instances():
    try:
        response = ec2.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                print(f"Instance ID: {instance['InstanceId']}")
                print(f"Instance State: {instance['State']['Name']}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    describe_instances()
