import boto3

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')


def get_all_employees():
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

get_all_employees()


# for displaying specific employee

# def get_employee(employee_id):
#     table = dynamodb.Table('Employees')
#     response = table.get_item(
#         Key={
#             'employee_id': employee_id
#         }
#     )
#     item = response.get('Item')
#     if item:
#         print("Employee retrieved successfully:", item)
#     else:
#         print("Employee not found.")
#     return item
# Get an employee
# get_employee(1)





