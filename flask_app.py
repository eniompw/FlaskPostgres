from flask import Flask, request
app = Flask(__name__)

import os
DATABASE_URL = os.environ['DATABASE_URL']
import psycopg2
con = psycopg2.connect(DATABASE_URL, sslmode='require')

@app.route('/')
def hello_world():
    return 'Postgres'

@app.route('/create')
def create():
	cur = con.cursor()
	cur.execute("""	CREATE TABLE Users(
				Username VARCHAR(20) NOT NULL PRIMARY KEY,
				Password VARCHAR(20) NOT NULL
					  )
		    """)
	con.commit()
	return 'CREATE'

@app.route('/insert')
def insert():
	cur = con.cursor()
	cur.execute("""	INSERT INTO Users VALUES ('Bob', '123') """)
	con.commit()
	return 'INSERT'

@app.route('/inget')
def inget():
	cur = con.cursor()
	un = request.args.get('un', '')
	pw = request.args.get('pw', '')
	cur.execute("INSERT INTO Users VALUES (%s,%s)", (un,pw))
	con.commit()
	return 'inserted get'

@app.route('/select')
def select():
	cur = con.cursor()
	cur.execute("SELECT * FROM Users")
	return str(cur.fetchall())

@app.route('/delete')
def delete():
	cur = con.cursor()
	cur.execute("""	DELETE FROM Users """)
	con.commit()
	return 'DELETE'

