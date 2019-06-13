import psycopg2
from flask import Flask, jsonify, request
# app.debug = True

app = Flask(__name__)

conn = psycopg2.connect(host="localhost",
                        database="pet_hotel"
                        )

cur = conn.cursor()


cur.execute('SELECT * FROM pet')
cur.fetchone()

@app.route('/pet', methods=['GET', 'POST', 'PUT', 'DELETE'])
def petRoutes():
  if request.method == 'GET':
	  cur.execute('SELECT * FROM pet JOIN owner ON owner.id=pet.owner_id')
	  rows = jsonify(cur.fetchall())
	  print(rows)
	  return rows

  # else:
  #   print('hey')
  #   return 200
  elif request.method == 'POST':
    cur.execute('INSERT INTO pet (name, owner_id, breed, color, checked_in, date_in) VALUES(%s,%s,%s,%s,%s,%s)',('fluffy','1','cotton mouth','black','True','06/12/2019'))
    print('hey')
    return 'OK',200
  
# @app.route('/owner', methods=['GET', 'POST', 'DELETE'])
cur.execute('SELECT * FROM pet')
rows = cur.fetchall()
print(rows)

conn.commit()
  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'


conn.commit()
