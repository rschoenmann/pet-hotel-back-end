import psycopg2
from flask import Flask, jsonify, request
app = Flask(__name__)

conn = psycopg2.connect(host="localhost",
                        database="pet_hotel"
                        )

cur = conn.cursor()


cur.execute('SELECT * FROM pet')
cur.fetchone()

@app.route('/', methods=['GET', 'POST'])
def getPet():
	if request.method == 'GET':
		cur.execute('SELECT * FROM pet')
		rows = jsonify(cur.fetchall())
		print(rows[0])
		return jsonify(rows)
		

cur.execute('SELECT * FROM pet')
rows = cur.fetchall()
print(rows)

conn.commit()
  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'


conn.commit()
