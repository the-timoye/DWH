from aws.helpers import (create_aws_clients,
                         delete_cluster,
                         delete_role,
                         check_cluster_status)


def main():
    iam_client = create_aws_clients('iam')
    redshift_client = create_aws_clients('redshift')
    cluster_status = check_cluster_status(redshift_client)
    if cluster_status == 'available':
        delete_cluster(redshift_client)
    elif cluster_status == 'deleting':
        while cluster_status == 'deleting':
            print('============== DELETING CLUSTER ==============')
            print('Status check: ', cluster_status)
            cluster_status = check_cluster_status(redshift_client)
    else:
        print('No cluster found: ', cluster_status)

    delete_role(iam_client, 'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess')


if __name__ == '__main__':
    main()
