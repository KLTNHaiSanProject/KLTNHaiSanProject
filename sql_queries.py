
from configs.db_credentials import database_target
from configs.db_credentials import database_source
from extracts import tina_sql_queries as tina
from transform import transform_tina
from loads import tina_load
import psycopg2


try:
    for database in database_source:
        connection = psycopg2.connect(**database)
       
        table = tina.getAllData(connection)
        transform_tina.transform_etl_generic(table)
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    print('')





try:
    connection = psycopg2.connect(**database_target)
    
    print(table)
    tina_load.writedata(connection,table)
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    print('')
