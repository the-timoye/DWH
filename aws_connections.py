from config import KEY, SECRET, ROLE_NAME as ROLE, CLUSTER_ID, DATABASE, DATABASE_USER, DATABASE_PASSWORD, DATABASE_PORT
from aws.helpers import create_aws_clients, create_aws_resource, attach_role_policy, create_cluster, allow_cluster_ingress, create_iam_role, check_cluster_status

def main():
    # Define boto3 clients for IAM & Redshift
    print('============== CREATING AWS CLIENTS ==============')
    iam_client = create_aws_clients('iam')
    redshift_client = create_aws_clients('redshift')
    ec2_client = create_aws_resource('ec2')

    print('============== CREATING IAM ROLE ==============')
    create_iam_role(iam_client, ROLE)

    print('============== ATTACHING ROLE POLICY ==============')
    attach_role_policy(iam_client, ROLE)

    print('============== GET ROLE ARN ==============')
    roleArn = iam_client.get_role(RoleName=ROLE)['Role']['Arn']
    print(roleArn)

    print('============== CREATING REDSHIFT CLIENT ==============')
    create_cluster(redshift_client, roleArn)

    print('============== DESCRIBE REDSHIFT CLIENT ==============')
    cluster = redshift_client.describe_clusters(ClusterIdentifier=CLUSTER_ID)['Clusters'][0]
    cluster_status = cluster['ClusterStatus']

    print('============== CHECKING CLUSTER STATUS ==============')
    cluster_status = check_cluster_status(redshift_client)
    while cluster_status != 'available':
        print('Status check: ', cluster_status)
        cluster_status = check_cluster_status(redshift_client)

    print('============== OPEN CLUSTERS TCP PORT FOR INCOMING ACCESS ==============')
    allow_cluster_ingress(ec2_client, cluster)

    cluster_address = cluster['Endpoint']['Address']
    cluster_role_arn = cluster['IamRoles'][0]['IamRoleArn']
    print('Cluster Address = ', cluster_address)
    print('Cluster Role Arn = ', cluster_role_arn)

if __name__ == "__main__":
    main()