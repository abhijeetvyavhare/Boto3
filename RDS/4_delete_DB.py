import boto3

rds = boto3.client('rds')

def delete_db_instance():
    response = rds.delete_db_instance(
        DBInstanceIdentifier='mydatabase',
        SkipFinalSnapshot=True  # Skip the final snapshot
    )
    print("Delete DB Instance Response:", response)

if __name__ == "__main__":
    delete_db_instance()
