import mysql.connector

class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='root' ,
            database='flights',
            auth_plugin="mysql_native_password"

            )
            self.cursor = self.conn.cursor()
            print('Connected to the database')
        except:
            print('Cannot connect to the database')

    def fetch_city_names(self):
        city=[]
        self.cursor.execute('''
        SELECT DISTINCT(Destination) FROM flights.flights
                            UNION
                            SELECT DISTINCT(Source) FROM flights.flights'''
                            )
        result = self.cursor.fetchall()
        for item in result:
            city.append(item[0])
        
        return city

        

        
