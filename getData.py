import json
import names
import psycopg2
from faker import Faker
import decimal
import requests


def getData():
    r = requests.get(url='http://127.0.0.1:5000')
    data = r.content
    res = json.loads(data.decode('utf-8'))
    name = res['name']
    surname = res['lastname']
    address = res['address']
    birthday = res['birthday']
    lat = res['latitude']
    lng = res['longitude']

    return name, surname, address, birthday, lat, lng

DB_NAME = 'jlbbczcg'
DB_USER = 'jlbbczcg'
DB_PASS = '5hObYSSHb3Nha6yPNjGjMyRwqeh71qMy'
DB_HOST = 'tyke.db.elephantsql.com'
DB_PORT = '5432'

conn = psycopg2.connect(database = DB_NAME, user = DB_USER,
                        password = DB_PASS, host = DB_HOST,
                        port = DB_PORT)

cur = conn.cursor()

name, surname, address, birthday, lat, lng = getData()
#INSERT DATA TO DB TABLE
cur.execute(
    "INSERT INTO Personal (NAME, SURNAME, ADDRESS, BIRTHDAY, LATITUDE, LONGITUDE)"
    " Values(%s, %s, %s, %s, %s, %s)", (name, surname, address, birthday, lat, lng)
)

conn.commit()
conn.close()

