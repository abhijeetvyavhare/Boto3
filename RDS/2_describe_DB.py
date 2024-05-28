import boto3

rds = boto3.client('rds')

def describe_db_instance():
    response = rds.describe_db_instances(
        DBInstanceIdentifier='mydatabase'
    )
    print("Describe DB Instance Response:", response)

if __name__ == "__main__":
    describe_db_instance()
