import boto3

rds = boto3.client('rds')

def create_db_instance():
    db_instance_identifier = input("Enter DB instance identifier: ")
    db_name = input("Enter database name: ")
    master_username = input("Enter master username: ")
    master_user_password = input("Enter master user password: ")
    
    response = rds.create_db_instance(
        AllocatedStorage=5,
        DBInstanceClass='db.t3.micro',
        DBInstanceIdentifier=db_instance_identifier,
        DBName=db_name,
        Engine='mysql',
        EngineVersion='8.0.35',
        LicenseModel='general-public-license',
        MasterUserPassword=master_user_password,
        MasterUsername=master_username,
    )
    print(f"DB Instance '{db_instance_identifier}' created successfully.")
    print(f"DB Instance ARN: {response['DBInstance']['DBInstanceArn']}")

def describe_db_instance():
    db_instance_identifier = input("Enter DB instance identifier: ")
    response = rds.describe_db_instances(
        DBInstanceIdentifier=db_instance_identifier
    )
    db_instance = response['DBInstances'][0]
    print(f"DB Instance Identifier: {db_instance['DBInstanceIdentifier']}")
    print(f"DB Instance Status: {db_instance['DBInstanceStatus']}")
    print(f"DB Instance Endpoint: {db_instance['Endpoint']['Address']}")
    print(f"DB Instance Port: {db_instance['Endpoint']['Port']}")
    print(f"Allocated Storage: {db_instance['AllocatedStorage']} GB")

def modify_db_instance():
    db_instance_identifier = input("Enter DB instance identifier: ")
    new_allocated_storage = int(input("Enter new allocated storage (in GB): "))
    
    response = rds.modify_db_instance(
        DBInstanceIdentifier=db_instance_identifier,
        AllocatedStorage=new_allocated_storage,
        ApplyImmediately=True
    )
    print(f"DB Instance '{db_instance_identifier}' modified successfully.")
    print(f"New Allocated Storage: {new_allocated_storage} GB")

def delete_db_instance():
    db_instance_identifier = input("Enter DB instance identifier: ")
    
    response = rds.delete_db_instance(
        DBInstanceIdentifier=db_instance_identifier,
        SkipFinalSnapshot=True  # Skip the final snapshot
    )
    print(f"DB Instance '{db_instance_identifier}' deleted successfully.")

def menu():
    while True:
        print("\nRDS Management Menu")
        print("1. Create DB Instance")
        print("2. Describe DB Instance")
        print("3. Modify DB Instance")
        print("4. Delete DB Instance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_db_instance()
        elif choice == '2':
            describe_db_instance()
        elif choice == '3':
            modify_db_instance()
        elif choice == '4':
            delete_db_instance()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
