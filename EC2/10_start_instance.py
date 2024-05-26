import boto3

ec2 = boto3.client('ec2')

def start_instance(instance_id):
    try:
        response = ec2.start_instances(
            InstanceIds=[instance_id],
        )
        print(f"Starting instance: {instance_id}")
        for instance in response['StartingInstances']:
            print(f"Instance ID: {instance['InstanceId']}, Current State: {instance['CurrentState']['Name']}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    instance_id = input("Enter instance ID: ")
    start_instance(instance_id)
