import psycopg2
import psycopg2.extras

# import pprint

from flask import Flask, jsonify, request
app = Flask(__name__)

conn = psycopg2.connect(host="localhost",
                        database="pet_hotel"
                        )

cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


cur.execute('SELECT * FROM pet')
cur.fetchone()
# pprint.pprint(cur.description[0].type_code)
# column_names = [desc[0] for desc in cur.description]

@app.route('/', methods=['GET', 'POST'])
def getPet():
	if request.method == 'GET':
		cur.execute('SELECT * FROM pet')
    
		rows = jsonify(cur.fetchall())
		print(rows)
		return (rows)




cur.execute('SELECT * FROM pet')
rows = cur.fetchall()
print(rows)

conn.commit()


@app.route('/greet')
def say_hello():
  return 'Hello from Server'
