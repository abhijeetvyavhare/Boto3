import boto3

ec2 = boto3.client('ec2')

def terminate_instance(instance_id):
    try:
        response = ec2.terminate_instances(InstanceIds=[instance_id])
        print(f"Terminating Instance: {instance_id}")
        print(response)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    instance_id = input("Enter instance ID: ") 
    terminate_instance(instance_id)
