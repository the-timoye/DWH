import psycopg2
from aws.helpers import create_aws_clients
from config import KEY, SECRET, ROLE_NAME as ROLE, CLUSTER_ID, DATABASE, DATABASE_USER, DATABASE_PASSWORD, DATABASE_PORT

redshift_client = create_aws_clients('redshift')
cluster = redshift_client.describe_clusters(ClusterIdentifier=CLUSTER_ID)['Clusters'][0]
cluster_address = cluster['Endpoint']['Address']

def main():
    print('============== CONNECT DATABASE ==============')
    try:
        connection = psycopg2.connect(
        host=cluster_address,
        database=DATABASE,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD)
        cursor = connection.cursor()
        print('database connected.')
        return cursor

    except Exception as e:
        print('Database Connection Error:', e)

if __name__ == "__main__":
    main()