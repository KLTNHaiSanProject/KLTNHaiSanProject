import petl as etl
import psycopg2
from datetime import timezone
def transform_etl_generic(table):
    etl.convert(table,'ngayud', )