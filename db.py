import psycopg2

DB_NAME = 'jlbbczcg'
DB_USER = 'jlbbczcg'
DB_PASS = '5hObYSSHb3Nha6yPNjGjMyRwqeh71qMy'
DB_HOST = 'tyke.db.elephantsql.com'
DB_PORT = '5432'

conn = psycopg2.connect(database = DB_NAME, user = DB_USER,
                        password = DB_PASS, host = DB_HOST,
                        port = DB_PORT)

cur = conn.cursor()
#CREATE DB TABLE

cur.execute(
    """
    CREATE TABLE Personal
    (
    ID INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    SURNAME TEXT NOT NULL,
    ADDRESS TEXT NOT NULL,
    BIRTHDAY TEXT NOT NULL,
    LATITUDE DECIMAL NOT NULL,
    LONGITUDE DECIMAL NOT NULL
    )
    """
)

conn.commit()
conn.close()