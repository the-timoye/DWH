import configparser
config = configparser.ConfigParser()
config.read_file(open('./config.py'))

KEY = config.get('AWS','KEY')
SECRET = config.get('AWS', 'SECRET')
REGION = config.get('AWS', 'REGION')
ARN = config.get('AWS', 'ARN')

ROLE_NAME=config.get('DWH','ROLE_NAME')
CLUSTER_ID=config.get('DWH', 'CLUSTER_ID')

DATABASE_PORT=config.get('DWH', 'DATABASE_PORT')
DATABASE_USER=config.get('DWH', 'DATABASE_USER')
DATABASE=config.get('DWH', 'DATABASE')
DATABASE_PASSWORD=config.get('DWH', 'DATABASE_PASSWORD')

LOG_JSONPATH = config.get('S3', 'LOG_JSONPATH')
SONG_DATA = config.get('S3', 'SONG_DATA')
LOG_DATA =config.get('S3', 'LOG_DATA')

