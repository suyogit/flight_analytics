import mysql.connector

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='root' ,
        auth_plugin="mysql_native_password"

        #database='airlines'
        )
    cursor = conn.cursor()
    print('Connected to the database')
except:
    print('Cannot connect to the database')

#Create a database 
# cursor.execute('CREATE DATABASE IF NOT EXISTS airlines')
# conn.commit()

#create table
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS airlines(
#     airport_id INT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     city VARCHAR(255) NOT NULL,
#     code VARCHAR(255) NOT NULL)
# ''')
# conn.commit()

# Insert data
# cursor.execute('''
# INSERT INTO airlines(airport_id, name, city, code)
# VALUES(1, 'Tribhuvan International Airport', 'KTM', 'TIA'),
#                (2, 'Pokhara International Airport','PKR', 'PIA'),
#                 (3, 'Bhairahawa International Airport', 'BWA', 'BIA'),
#                 (4, 'Nepalgunj International Airport', 'NGJ', 'NIA'),
#                 (5, 'Biratnagar International Airport', 'BRT', 'BIA')
               
# ''')
# conn.commit()



# Read data
# cursor.execute('SELECT * FROM airlines WHERE airport_id>2 ' )
# result = cursor.fetchall() #returns a list of tuples, if we use  fetch only one then it returns a tuple
#print(result)
# for data in result:
#     print(data[3])


# # Update data
# cursor.execute('''
# UPDATE airlines
# SET code = 'BTIA'
# WHERE airport_id = 5
# ''')
# conn.commit()


# Delete data
# cursor.execute('''
# DELETE FROM airlines
# WHERE airport_id = 5
# ''')
# conn.commit()
