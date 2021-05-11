from flask import Flask, request
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

@app.route('/in')
def inget():
	cur = con.cursor()
	un = request.args.get('un', '')
	pw = request.args.get('pw', '')
	cur.execute("INSERT INTO Users VALUES (%s,%s)", (un,pw))
	con.commit()
	return 'inserted get'

@app.route('/fo')
def fo():
	cur = con.cursor()
	cur.execute("SELECT * FROM Users")
	return cur.fetchone()

@app.route('/select')
def select():
	cur = con.cursor()
	cur.execute("SELECT * FROM Users")
	result = cur.fetchall()
	if len(result) == 0:
		return 'no records'
	else:
		return ','.join(map(str, result))

@app.route('/delete')
def delete():
	cur = con.cursor()
	cur.execute("""	DELETE FROM Users """)
	con.commit()
	return 'DELETE'

