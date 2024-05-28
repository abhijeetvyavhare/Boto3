# AWS Automation with Boto3

Welcome to the AWS Automation with Boto3 repository! This collection of scripts is designed to help you manage various AWS services efficiently using Python and the Boto3 library. Whether you're just getting started with AWS or looking to automate your cloud operations, these scripts can serve as a valuable resource.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [EC2 (Elastic Compute Cloud)](#ec2-elastic-compute-cloud)
  - [DynamoDB](#dynamodb)
  - [IAM (Identity and Access Management)](#iam-identity-and-access-management)
  - [RDS (Relational Database Service)](#rds-relational-database-service)
  - [S3 (Simple Storage Service)](#s3-simple-storage-service)
  - [VPC (Virtual Private Cloud)](#vpc-virtual-private-cloud)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get started with these scripts, you'll need:

- An AWS account with appropriate permissions
- AWS CLI configured with your credentials
- Python installed on your machine
- Boto3 library installed

## Prerequisites

Ensure you have the following installed and configured:

- **AWS CLI**: Configure it with your credentials by running `aws configure`.
- **Python**: Install the latest version from [python.org](https://www.python.org/).
- **Boto3**: Install it using pip:
  ```bash
  pip install boto3
  ```

## Installation

Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/aws-automation-boto3.git
cd aws-automation-boto3
```

## Usage

Each directory contains scripts related to a specific AWS service. Below are the details for each service:

### EC2 (Elastic Compute Cloud)
Scripts for managing EC2 instances, security groups, and key pairs.
- `10_start_instance.py`
- `1_security_group.py`
- `2_add_inbound_rule.py`
- `3_create_key_pair.py`
- `4_list_key_pair.py`
- `5_delete_key_pair.py`
- `6_launch_instance.py`
- `7_list_instances.py`
- `8_stop_instance.py`
- `9_terminate_instance.py`

### DynamoDB
Scripts for managing DynamoDB tables and items.
- `0_menu_driven.py`
- `1_create_table.py`
- `2_insert_item.py`
- `3_update_item.py`
- `4_display_item.py`
- `5_delete_item.py`
- `6_delete_table.py`

### IAM (Identity and Access Management)
Scripts for managing IAM users, groups, and roles.
- `0_menu_driven.py`
- `add_user_to_group.py`
- `group_create.py`
- `group_delete.py`
- `list_user_in_group.py`
- `remove_user_from_group.py`
- `role_attach_policy.py`
- `role_create.py`
- `role_delete.py`
- `role_detach_policy.py`
- `user_attachpolicy.py`
- `user_create.py`
- `user_delete.py`
- `user_detachpolicy.py`
- `user_list.py`

### RDS (Relational Database Service)
Scripts for managing RDS instances and databases.
- `0_menu_driven.py`
- `1_create_table.py`
- `2_describe_db.py`
- `3_update_db.py`
- `4_delete_db.py`

### S3 (Simple Storage Service)
Scripts for managing S3 buckets and objects.
- `0_menu_driven.py`
- `1_create_bucket.py`
- `2_list_bucket.py`
- `3_upload_object.py`
- `4_upload_object_from_url.py`
- `5_list_objects.py`
- `6_delete_object.py`
- `7_copy_object.py`
- `8_move_object.py`
- `9_delete_bucket.py`

### VPC (Virtual Private Cloud)
Scripts for managing VPCs, subnets, and route tables.
- `0_vpc_operations.py`
- `1_create_vpc.py`
- `2_igw.py`
- `3_create_subnet.py`
- `4_public_route_table.py`
- `5_private_route_table.py`
- `6_route_table_association.py`

## Contributing

Contributions are welcome! If you have scripts or examples that you think would be useful additions, please submit a pull request. Ensure your code follows the repository's style guidelines and includes proper documentation.

