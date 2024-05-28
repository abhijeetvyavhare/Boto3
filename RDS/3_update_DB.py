import boto3

rds = boto3.client('rds')

def modify_db_instance():
    response = rds.modify_db_instance(
        DBInstanceIdentifier='mydatabase',
        AllocatedStorage=10,  # Increase storage
        ApplyImmediately=True
    )
    print("Modify DB Instance Response:", response)

if __name__ == "__main__":
    modify_db_instance()
