from config import KEY, SECRET, REGION, ROLE_NAME as ROLE, CLUSTER_ID
from aws.helpers import create_aws_clients, create_aws_resource, attach_role_policy, create_cluster


def main():
    # Define boto3 clients for IAM & Redshift
    print('============== CREATING AWS CLIENTS ==============')
    iam_client = create_aws_clients('iam')
    redshift_client = create_aws_clients('redshift')
    ec2_client = create_aws_resource('ec2')

    print('============== ATTACHING ROLE POLICY ==============')
    attach_role_policy(iam_client)

    print('============== GET ROLE ARN ==============')
    roleArn = iam_client.get_role(RoleName=ROLE)
    print(roleArn)

    print('============== CREATING REDSHIFT CLIENT ==============')
    create_cluster(redshift_client, roleArn)

    print('============== DESCRIBE REDSHIFT CLIENT ==============')
    cluster = {'ClusterStatus': 'creating'}

    while cluster['ClusterStatus'] != 'available':
        print('============== CHECKING CLUSTER STATUS ==============')
        cluster['ClusterStatus'] = redshift_client.describe_clusters(ClusterIdentifier=CLUSTER_ID)['Clusters'][0]
        print(cluster)
        

    print('============== OPEN CLUSTERS TCP PORT FOR INCOMING ACCESS ==============')


if __name__ == "__main__":
    main()