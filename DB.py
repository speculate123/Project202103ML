import psycopg2
import config

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
except:
    print ("Failed to connect to database.")