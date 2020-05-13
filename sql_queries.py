
from configs.db_credentials import database_target
from configs.db_credentials import database_source
import psycopg2

try:
    for database in database_source:
        connection = psycopg2.connect(**database)
        cursor = connection.cursor()
        cursor.execute("select version();")
        record = cursor.fetchone()
        print(record)
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    print('')
