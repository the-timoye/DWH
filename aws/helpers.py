import boto3
import json
from config import KEY, SECRET, REGION, ROLE_NAME, DATABASE, DATABASE_PORT, DATABASE_USER, DATABASE_PASSWORD, CLUSTER_ID, NODE_TYPE, NUMBER_OF_NODES, CLUSTER_TYPE

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

def create_iam_role(client, ROLE, ):
    try:
        return client.create_role(
            Path='/',
            RoleName=ROLE,
            Description='Allows Redshift clusters to call AWS services on your behalf.',
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
        return redshift_client.create_cluster(
            ClusterType=CLUSTER_TYPE,
            NodeType=NODE_TYPE,
            NumberOfNodes=int(NUMBER_OF_NODES) ,
            DBName=DATABASE,
            ClusterIdentifier=CLUSTER_ID,
            MasterUsername=DATABASE_USER,
            MasterUserPassword=DATABASE_PASSWORD,
            IamRoles=[roleArn]
        )
    except Exception as e:
        print('An error occured while creating cluster')
        print(e)

def attach_role_policy(iam_client, role):
    try:
        return iam_client.attach_role_policy(
        RoleName=role,
        PolicyArn="arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
                      )['ResponseMetadata']['HTTPStatusCode']
    except Exception as e:
        print('Error attaching role policy', e)

def allow_cluster_ingress(ec2_client, cluster):
    try:
        vpc = ec2_client.Vpc(id = cluster['VpcId'])
        default_security_group = list(vpc.security_groups.all())[0]
        print(default_security_group)

        default_security_group.authorize_ingress(
            GroupName = default_security_group.group_name,
            CidrIp = '0.0.0.0/0',
            IpProtocol = 'TCP',
            FromPort = int(DATABASE_PORT),
            ToPort = int(DATABASE_PORT)
        )
    except Exception as e:
        print('Error opening TCP port: ', e)