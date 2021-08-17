# ETL PIPELEINE FOR SPARKIFY DATABASE

## The Problem

Sparkify, a movie streaming app decides to have their user data stored in the cloud for easy data analysis.
The data currently is stored in an Amazon S3 buckets in JSON files.


## The Solution
This project allows easy analysis of Sparkify's data by:
    - Building an ETL pipeline to extract data from the S3 bucket
    - Staging the data in Amazon Redshift
    - Transforming the data into a set of dimensional tables for easier analysis.
    
    
## FOLDER & FILE CONTENTS

    A. sql (folder): contains all drop, copy, and insert queries to complete the ETL process.
        Also contains the ```connect_database``` function. <br>
    
    B. aws_connections.py: This creates roles, cluster, attaches role policy and opens cluster's TCP port. Your cluster and ARN is also stored in your config file. <br>
    
    C. etl.py: the functions here run the `COPY` and `INSERT` query statements in the sql_queries.py file <br>

    D. aws_disconnections.py: Contains functions to delete created role, detach policies and delete cluster

    E. config.py: extracts all needed keys from configuration file

    F. aws (folder): contains functions that use the boto3 library to create and delete roles, users, and clusters
    
    
## RUNNING THE SCRIPTS

Before running these scripts, ensure you have created a User and a Role in the IAM section of your AWS console with S3 read-only access, and Redshift Cluster with an open TCP port allowing traffic to and from the Database's port.

Once these are confirmed, be sure to include the following in your config file:
    - HOST
    - DB_NAME
    - DB_USER
    - DB_PASSWORD
    - DB_PORT
    - ARN
    - ROLE_NAME
    
#### Step 1:
    create redshift client with ```aws_connections.py```
    This creates roles, cluster, attaches role policy and opens cluster's TCP port
    Your cluster and ARN is also stored in your config file.

### Step 2:
    Run the etl.py file in your terminal.
    Here, data in the S3 buckets are copied to the staging tables created above.
    At the end of the insert operation, you will be required to input a 'Y' or 'N'. This determins if you would like to run the ```SELECT``` queries on your newly created warehouse.
### Step 3:
    Run `aws_disconnections.py` to delete cluster and role created
    

## The Schema
The dimensional tables generated from the dataset are as follows:


### Songplays Table

    - Description: records in event data associated with song plays
    - Table Type: Fact table
    - Columns:

        | column name |  datatype |
        |-------------|-----------|
        | songplay_id |  IDENTITY |
        |  start_time | TIMESTAMP |
        |     user_id |   INTEGER |
        |       level |   VARCHAR |
        |     song_id |   VARCHAR |
        | artist_id   | VARCHAR   |
        | session_id  | INT       |
        | location    | VARCHAR   |
        | user_agent  | VARCHAR   |
        
        
### Users Table

    - Description: users in the app
    - Table Type: Dimension  table
    - Columns:
    
        | column name | datatype |
        |-------------|----------|
        |     user_id |  INTEGER |
        |      gender |  VARCHAR |
        |  first_name |  VARCHAR |
        |   last_name |  VARCHAR |
        |       level |  VARCHAR |
        
### Artists Table
    - Description: artists in music database
    - Table Type: Dimension  table
    - Columns:
        | column name | datatype |
        |-------------|----------|
        |   artist_id |  VARCHAR |
        |        name |  VARCHAR |
        |    location |  VARCHAR |
        |    latitude |  NUMERIC |
        |   longitude |  NUMERIC |

### Time Table
    - Description: timestamps of records in songplays broken down into specific units
    - Table Type: Dimension  table
    - Columns:
        | column name |  datatype |
        |-------------|-----------|
        | start_time  | TIMESTAMP |
        | hour        |   INTEGER |
        | day         |   INTEGER |
        | week        |   INTEGER |
        | month       |   INTEGER |
        | year        | INTEGER   |
        | weekday     | INTEGER   |
        
### Songs Table
    - Description: songs in music database
    - Table Type: Dimension  table
    - Columns:
        | column name | datatype |
        |-------------|----------|
        | song_id     |  VARCHAR |
        | title       |  VARCHAR |
        | artist_id   |  VARCHAR |
        | year        |  INTEGER |
        | duration    |  NUMERIC |
        | year        | INTEGER  |
        | weekday     | INTEGER  |
