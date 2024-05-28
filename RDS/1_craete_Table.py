import boto3

rds = boto3.client('rds')

def create_db_instance():
    response = rds.create_db_instance(
        AllocatedStorage=5,
        DBInstanceClass='db.t3.micro',
        DBInstanceIdentifier='mydatabase',
        Engine='mysql',
        EngineVersion='8.0.35',
        LicenseModel='general-public-license',
        MasterUserPassword='password',
        MasterUsername='admin',
    )
    print("Create DB Instance Response:", response)

if __name__ == "__main__":
    create_db_instance()
