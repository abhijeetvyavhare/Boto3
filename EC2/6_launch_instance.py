# 6_EC2_CreateInstance.py

import boto3

ec2 = boto3.resource('ec2')

def create_instance(image_id, instance_type, key_name, security_group_ids, instance_name):
    try:
        instances = ec2.create_instances(
            ImageId=image_id,
            InstanceType=instance_type,
            KeyName=key_name,
            SecurityGroupIds=[security_group_ids],  # Pass as a list
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [{'Key': 'Name', 'Value': instance_name}]
                }
            ]
        )
        instance = instances[0]
        instance.wait_until_running()
        instance.load()  # Refresh instance attributes
        print(f"Instance Created: {instance.id}, Name: {instance_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    instance_type = 't2.micro'
    image_id = input("Enter image ID: ")
    key_name = input("Enter key pair name: ")
    security_group_ids = input("Enter security group ID: ")
    instance_name = input("Enter instance name: ")
    
    create_instance(image_id, instance_type, key_name, security_group_ids, instance_name)
