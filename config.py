import configparser

config = configparser.ConfigParser()
config.read_file(open('./dwh.cfg'))

KEY = config.get('AWS','KEY')
SECRET = config.get('AWS', 'SECRET')
REGION = config.get('AWS', 'REGION')

ROLE_NAME=config.get('DWH','ROLE_NAME')
CLUSTER_ID=config.get('DWH', 'CLUSTER_ID')
CLUSTER_TYPE=config.get('DWH', 'CLUSTER_TYPE')
NUMBER_OF_NODES=config.get('DWH', 'NUMBER_OF_NODES')
NODE_TYPE=config.get('DWH', 'NODE_TYPE')

DATABASE_PORT=config.get('DWH', 'DATABASE_PORT')
DATABASE_USER=config.get('DWH', 'DATABASE_USER')
DATABASE=config.get('DWH', 'DATABASE')
DATABASE_PASSWORD=config.get('DWH', 'DATABASE_PASSWORD')

LOG_JSONPATH = config.get('S3', 'LOG_JSONPATH')
SONG_DATA = config.get('S3', 'SONG_DATA')
LOG_DATA =config.get('S3', 'LOG_DATA')

