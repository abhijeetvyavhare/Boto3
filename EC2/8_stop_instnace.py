import boto3

ec2 = boto3.client('ec2')

def stop_instance(instance_id):
    try:
        response = ec2.stop_instances(InstanceIds=[instance_id])
        print(f"Stopping Instance: {instance_id}")
        print(response)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    instance_id = input("Enter instance ID: ") 
    stop_instance(instance_id)
