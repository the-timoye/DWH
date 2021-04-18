from config import KEY, SECRET, REGION, ROLE_NAME as ROLE, CLUSTER_ID, DATABASE, DATABASE_USER, DATABASE_PASSWORD, DATABASE_PORT
from aws.helpers import create_aws_clients, create_aws_resource, attach_role_policy, create_cluster, allow_cluster_ingress


def main():
    # Define boto3 clients for IAM & Redshift
    print('============== CREATING AWS CLIENTS ==============')
    iam_client = create_aws_clients('iam')
    redshift_client = create_aws_clients('redshift')
    ec2_client = create_aws_resource('ec2')

    print('============== ATTACHING ROLE POLICY ==============')
    attach_role_policy(iam_client)

    print('============== GET ROLE ARN ==============')
    roleArn = iam_client.get_role(RoleName=ROLE)['Role']['Arn']
    print(roleArn)

    print('============== CREATING REDSHIFT CLIENT ==============')
    create_cluster(redshift_client, roleArn)

    print('============== DESCRIBE REDSHIFT CLIENT ==============')
    cluster = redshift_client.describe_clusters(ClusterIdentifier=CLUSTER_ID)['Clusters'][0]
    cluster_status = cluster['ClusterStatus']
    cluster_address = cluster['Endpoint']['Address']
    cluster_role_arn = cluster['IamRoles'][0]['IamRoleArn']

    while cluster_status != 'available':
        print('============== CHECKING CLUSTER STATUS ==============')
        cluster_status = redshift_client.describe_clusters(ClusterIdentifier=CLUSTER_ID)['Clusters'][0]['ClusterStatus']
        print(cluster)


    print('============== OPEN CLUSTERS TCP PORT FOR INCOMING ACCESS ==============')
    allow_cluster_ingress(ec2_client, cluster)

    # create DB
    print('============== CREATE DATABASE ==============')
    # conn_string="postgresql://{}:{}@{}:{}/{}".format(
    #     DATABASE_USER,
    #     DATABASE_PASSWORD,
    #     cluster_address,
    #     DATABASE_PORT,
    #     DATABASE
    # )

if __name__ == "__main__":
    main()