import boto3

# Initialize a session using Amazon DynamoDB
dynamodb = boto3.resource('dynamodb')

def delete_employee(employee_id):
    table = dynamodb.Table('Employees')
    response = table.delete_item(
        Key={
            'employee_id': employee_id
        }
    )
    print("Employee deleted successfully:", response)

# Delete an employee
delete_employee(1)
