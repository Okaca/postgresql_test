import json
import names
from faker import Faker
import decimal
import requests

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)

def content():
    fake = Faker()
    address = fake.address()
    name = names.get_first_name()
    surname = names.get_last_name()

    birthdate = fake.profile('birthdate').get('birthdate')

    lat, lng = fake.profile('current_location').get('current_location')

    out_json = {
        'name' : name,
        'lastname' : surname,
        'address' : address,
        'birthday' : birthdate.isoformat(),
        'latitude' : lat,
        'longitude' : lng
    }

    requests.post(url='http://127.0.0.1:5000', data=json.dumps(out_json, cls = DecimalEncoder))

    print(json.dumps(out_json, cls = DecimalEncoder))

while requests.head(url = 'http://127.0.0.1:5000', timeout=5).status_code == 200:
    content()
