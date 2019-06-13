import psycopg2
import psycopg2.extras

from flask import Flask, jsonify, request
# app.debug = True

app = Flask(__name__)

conn = psycopg2.connect(host="localhost",
                        database="pet_hotel"
                        )

cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
conn.set_session(autocommit=True)


@app.route('/pet', methods=['GET', 'POST', 'PUT', 'DELETE'])
def petRoutes():
  if request.method == 'GET':
	  cur.execute('SELECT * FROM pet JOIN owner ON owner.id=pet.owner_id')
	  rows = jsonify(cur.fetchall())
	  print(rows)
	  return rows
    

  elif request.method == 'POST':
    # get an OK, but database isn't actually updating
    cur.execute('INSERT INTO pet (name, owner_id, breed, color, checked_in, date_in) VALUES(%s,%s,%s,%s,%s,%s)',('fluffy','1','cotton mouth','black','True','06/12/2019'))
    print('hey')
    return 'OK',200
  elif request.method == 'PUT':
    # get an OK, but database isn't actually updating
    cur.execute('UPDATE pet SET checked_in =%s WHERE id=%s',('FALSE','1'))
    return ('OK', 200)
  
@app.route('/owner', methods=['GET', 'POST', 'DELETE'])
def ownerRoutes():
	if request.method == 'GET':
		cur.execute('SELECT "owner"."id" AS "owner_id", "name", count(*) FROM "owner" JOIN "pet" ON "pet".owner_id = "owner".id GROUP BY "owner".id;')
		rows = jsonify(cur.fetchall())
		print(rows)
		return rows


  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'
