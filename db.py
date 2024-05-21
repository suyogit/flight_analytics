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
    
    def fetch_all_flights(self,source,destination):
        self.cursor.execute('''
        select Airline, Route, Dep_Time, Duration, Price From flights
        where Source = '{}' and destination ='{}'

        '''.format(source, destination))
        data = self.cursor.fetchall()
        return data

    def fetch_airline_frequency(self):
        airline= []
        frequency=[]
        self.cursor.execute(
            '''
            select Airline, COUNT(*) from flights
            group by Airline
            '''
        )
        data =self.cursor.fetchall()
        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline, frequency

        

        
