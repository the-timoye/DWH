from sql.sql_connection import connect_database
from sql.drop_queries import drop_table_queries
from sql.create_tables import create_table_queries
from sql.insert_queries import insert_queries
from sql.select_queries import select_queries



# connect database
db_connection = connect_database()
db_cursor = db_connection.cursor

# drop & create tables
print('================= DROP TABLES =================')
for query in drop_table_queries:
    db_cursor.execute(query)
    db_cursor.commit()

#  create tables
print('================= CREATE TABLES =================')
for query in create_table_queries:
    db_cursor.execute(query)
    db_cursor.commit()

# insert data into tables
print('================= INSERT INTO TABLES =================')
for query in insert_queries:
    db_cursor.execute(query)
    db_cursor.commit()

# run select queries
run_select_queries = str(input('Would you like to see sample data from the queries you just created? Y/N: '))
if run_select_queries.upper() == 'Y':
    for query_index, query in select_queries:
        print('======================= Query {}: {} ======================='.format(query_index, query['query_title']))
        db_cursor.execute(query['query'])
    db_connection.close()
    print('Completed.')
else:
    db_connection.close()
    print('Process completed!')