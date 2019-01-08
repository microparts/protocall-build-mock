import heroku3
import os

heroku = heroku3.from_key(os.environ['HEROKU_API_KEY'])

# app = heroku_conn.apps()['sharp-night-7758']

app = heroku_conn.create_app(name=os.environ['MOCK_APP_DOMAIN'], region_id_or_name='eu')
