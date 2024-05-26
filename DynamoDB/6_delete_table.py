import boto3

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')

def delete_table(table_name):
    table = dynamodb.Table(table_name)
    table.delete()
    print(f"Table '{table_name}' deleted successfully.")


delete_table('Employees')
