import  petl as elt
import psycopg2
from datetime import timezone
def getAllData(connection):
    string_query = 'select * from medibv.atc_generic'
    table=elt.fromdb(connection,string_query)
    
    return table['ngayud']
