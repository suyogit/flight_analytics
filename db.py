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

    def busy_airport(self):
        city=[]
        frequency=[]
        self.cursor.execute(
            '''
            select Source, count(*) from (select Source from flights
            union all
            select Destination from flights) t
            group by t.Source
            order by count(*) desc
            '''
        )
        data =self.cursor.fetchall()
        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city, frequency


    def daily_freq(self):
        date=[]
        frequency=[]
        self.cursor.execute(
            '''
            select Date_of_Journey, count(*) from flights
            group by Date_of_Journey
            '''
        )
        data =self.cursor.fetchall()
        for item in data:
            date.append(item[0])
            frequency.append(item[1])

        return date, frequency

        

        
