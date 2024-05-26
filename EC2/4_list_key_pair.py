import boto3

ec2 = boto3.client('ec2')

def describe_key_pairs():
    try:
        response = ec2.describe_key_pairs()
        for key_pair in response['KeyPairs']:
            print(f"Key Pair Name: {key_pair['KeyName']}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    describe_key_pairs()
