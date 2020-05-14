import petl as etl
import psycopg2

def writedata(conection, table):
    etl.todb(table,conection,'son',create=True)
