import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='' 
        )
    cursor = connection.cursor()
    print('Connected to the database')
except:
    print('Cannot connect to the database')
    