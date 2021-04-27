import psycopg2
from aws.helpers import create_aws_clients
from config import KEY, SECRET, ROLE_NAME as ROLE, CLUSTER_ID, DATABASE, DATABASE_USER, DATABASE_PASSWORD, DATABASE_PORT

redshift_client = create_aws_clients('redshift')
cluster = redshift_client.describe_clusters(ClusterIdentifier=CLUSTER_ID)['Clusters'][0]
cluster_address = cluster['Endpoint']['Address']

def connect_database():
    print('============== CONNECT DATABASE ==============')
    try:
        connection = psycopg2.connect(
        host=cluster_address,
        database=DATABASE,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD)
        print('database connected.')
        return connection

    except Exception as e:
        print('Database Connection Error:', e)
