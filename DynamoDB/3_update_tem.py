import boto3

# Initialize a session using Amazon DynamoDB
dynamodb = boto3.resource('dynamodb')

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
    print("Employee updated successfully.", response['Attributes'])

# Update an employee
update_employee(
    1,
    'SET salary = :val1',
    {':val1': 90000}
)
