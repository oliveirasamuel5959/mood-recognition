import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Admin123!',
)

cursor = dataBase.cursor()

cursor.execute('CREATE DATABASE recognition')

print('All Done!')

