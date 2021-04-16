import boto3
import json
from config import KEY, SECRET, REGION, ROLE_NAME

def create_aws_clients(client):
    try:
        return boto3.client(
            client,
            region_name=REGION,
            aws_access_key_id=KEY,
            aws_secret_access_key=SECRET
        )
    except Exception as e:
        print('An error occured while creating clients')
        print(e)

def create_aws_resource(resource):
    try:
        return boto3.resource(
            resource,
            region_name=REGION,
            aws_access_key_id=KEY,
            aws_secret_access_key=SECRET
        )
    except Exception as e:
        print('An error occured while creating clients')
        print(e)

def create_iam_role(client):
    try:
        return client.create_role(
            Path='/',
            RoleName='',
            Description='',
            AssumeRolePolicyDocument=json.dumps({
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {
                            "Service": [
                                "redshift.amazonaws.com"
                            ]
                        },
                        "Action": "sts:AssumeRole"
                    }
                ]
            }
        ) )
    except Exception as e:
        print('Error creating role')
        print(e)

def create_cluster(redshift_client, roleArn):
    try:
        redshift_response = redshift_client.create_cluster(
            ClusterType='',
            NodeType='',
            NumberOfNodes=3,
            DBName='',
            ClusterIdentifier='',
            MasterUsername='',
            MasterPassword='',
            IamRoles=[roleArn]
        )
    except Exception as e:
        print('An error occured while creating cluster')
        print(e)
    return redshift_response

def attach_role_policy(iam_client):
    try:
        return iam_client.attach_role_policy(
        RoleName='',
        PolicyArn="arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
                      )['ResponseMetadata']['HTTPStatusCode']
    except Exception as e:
        print('Error attaching role policy', e)
