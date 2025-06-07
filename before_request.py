import mysql.connector
from connection import *

def connected_database():
   dbHost, dbUser, dbPassword, dbDatabase = data_mysql()
   db = mysql.connector.connect(host=dbHost, user=dbUser, password=dbPassword, database=dbDatabase, auth_plugin='mysql_native_password')
   return db