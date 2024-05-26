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

# Create the table
table_name = 'Employees'
table = create_table(table_name)
