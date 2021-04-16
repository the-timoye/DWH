import configparser
config = configparser.ConfigParser()
config.read_file(open('./config.py'))

KEY = config.get('AWS','KEY')
SECRET = config.get('AWS', 'SECRET')
REGION = config.get('AWS', 'REGION')


ROLE_NAME=config.get('DWH','ROLE_NAME')
CLUSTER_ID=config.get('DWH', 'CLUSTER_ID')

