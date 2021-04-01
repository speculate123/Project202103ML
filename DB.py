import psycopg2
import config

class Database:
    def __init__(self):
        print('Init DB...')
        self.check(config.table, config.table_attr)
       
    def connect(self):
        print("Connecting to database:")
        try:
            connection = psycopg2.connect(
                database = config.database,
                user = config.user,
                password = config.password,
                host = config.host,
                port = config.port
            )
            cursor=connection.cursor()
            print("Database connected.")
            return connection
        except:
            print ("Failed to connect to database.")
            
    def check(self, table, table_attr):
        connection = self.connect()
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_name = %s
            """, table)
            if cursor.fetchone()[0] != 1:
                cursor.execute("CREATE TABLE %s (%s)" % (table, table_attr))
                with open('data/AAPL.csv', 'r') as row:
                    next(row)# Skip the header row.
                    cursor.copy_from(row, 'AAPL', sep=',')
                connection.commit() 
                cursor.close()
        connection.close()
        print("Done!")