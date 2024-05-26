import boto3

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')


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
    print("Employee inserted successfully:", response)

# Insert an employee
insert_employee(1, 'Abhijeet Vyavhare', 'Development', 75000)
insert_employee(2, 'prasad Dhobale', 'Testing', 60000)
insert_employee(3, 'Vinayak Bhoir', 'Development', 75000)
