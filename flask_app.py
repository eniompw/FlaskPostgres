from flask import Flask
app = Flask(__name__)

import os
import psycopg2
DATABASE_URL = os.environ['DATABASE_URL']
con = psycopg2.connect(DATABASE_URL, sslmode='require')

@app.route('/')
def hello_world():
    return 'Postgres'

@app.route('/create')
def create():
	cur = con.cursor()
	cur.execute(	"""	CREATE TABLE Users(
					Username VARCHAR(20) NOT NULL PRIMARY KEY,
					Password VARCHAR(20) NOT NULL
						                  )
			""")
	con.commit()
	return 'CREATE'
