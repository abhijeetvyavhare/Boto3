import boto3

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')

def create_table(table_name):
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'employee_id',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'employee_id',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Wait until the table exists
    table.meta.client.get_waiter('table_exists').wait(TableName='Employees')
    print("Table created successfully.")
    return table

def insert_employee(employee_id, employee_name, department, salary):
    table = dynamodb.Table('Employees')
    response = table.put_item(
        Item={
            'employee_id': employee_id,
            'employee_name': employee_name,
            'department': department,
            'salary': salary
        }
    )
    print("Employee inserted successfully.")

def get_employee(employee_id):
    table = dynamodb.Table('Employees')
    response = table.get_item(
        Key={
            'employee_id': employee_id
        }
    )
    item = response.get('Item')
    if item:
        print(f" ID: {item['employee_id']}, Name: {item['employee_name']}, Department: {item['department']}, Salary: {item['salary']} ")
    else:
        print("Employee not found.")

def display_all_employees():
    table = dynamodb.Table('Employees')
    response = table.scan()
    items = response.get('Items')
    if items:
        print("Employees retrieved successfully:")
        for item in items:
            print(f" ID: {item['employee_id']}, Name: {item['employee_name']}")
            # print(f" ID: {item['employee_id']}, Name: {item['employee_name']}, Department: {item['department']}, Salary: {item['salary']} ")
    else:
        print("No employees found.")

def update_employee(employee_id, update_expression, expression_attribute_values):
    table = dynamodb.Table('Employees')
    response = table.update_item(
        Key={
            'employee_id': employee_id
        },
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values,
        ReturnValues="UPDATED_NEW"
    )
    print("Employee updated successfully.")

def delete_employee(employee_id):
    table = dynamodb.Table('Employees')
    response = table.delete_item(
        Key={
            'employee_id': employee_id
        }
    )
    print("Employee deleted successfully.")

def delete_all_items(table_name):
    table = dynamodb.Table(table_name)
    scan = table.scan()
    with table.batch_writer() as batch:
        for each in scan['Items']:
            batch.delete_item(
                Key={
                    'employee_id': each['employee_id']
                }
            )
    print("All items deleted from the table.")

def delete_table(table_name):
    delete_all_items(table_name)  # Delete all items first
    table = dynamodb.Table(table_name)
    table.delete()
    print(f"Table '{table_name}' deleted successfully.")

def main():
    while True:
        print("\nMENU")
        print("1. Create Table")
        print("2. Insert Employee")
        print("3. Get Employee Details")
        print("4. Display All Employees")
        print("5. Update Employee Details")
        print("6. Delete Employee")
        print("7. Delete Table")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            table_name=input("Enter table name: ")
            create_table(table_name)
        elif choice == '2':
            employee_id = int(input("Enter employee ID: "))
            employee_name = input("Enter employee name: ")
            department = input("Enter department: ")
            salary = int(input("Enter salary: "))
            insert_employee(employee_id, employee_name, department, salary)
        elif choice == '3':
            employee_id = int(input("Enter employee ID: "))
            get_employee(employee_id)
        elif choice == '4':
            display_all_employees()
        elif choice == '5':
            employee_id = int(input("Enter employee ID: "))
            attribute_name=input("Enter attribute name you want to update: ")
            update_expression = f"SET {attribute_name} = :val1"
            expression_attribute_values = {':val1': int(input("Enter new value: "))}
            update_employee(employee_id, update_expression, expression_attribute_values)
        elif choice == '6':
            employee_id = int(input("Enter employee ID: "))
            delete_employee(employee_id)
        elif choice == '7':
            confirm = input("WARNING: Deleting the table will delete all its items. Do you want to continue? (yes/no): ")
            if confirm.lower() == 'yes':
                delete_table('Employees')
            else:
                print("Table deletion cancelled.")
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
