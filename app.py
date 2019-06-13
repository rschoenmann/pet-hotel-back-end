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

cur.execute('SELECT * FROM pet')
cur.fetchone()

@app.route('/pet', methods=['GET', 'POST', 'PUT', 'DELETE'])
def petRoutes():
  if request.method == 'GET':
	  cur.execute('SELECT * FROM owner JOIN pet ON owner.id=pet.owner_id')
	  rows = jsonify(cur.fetchall())
	  print(rows)
	  return rows
    

  elif request.method == 'POST':
    # get an OK, but database isn't actually updating
    cur.execute('INSERT INTO pet (pet_name, owner_id, breed, color, checked_in, date_in) VALUES(%s,%s,%s,%s,%s,%s)',('fluffy','1','cotton mouth','black','True','06/12/2019'))
    print('hey')
    return 'OK',200


@app.route('/pet/<int:id>', methods=['PUT', 'DELETE'])
def petDeletePut(id):
  if request.method == 'PUT':
    # get an OK, but database isn't actually updating
    cur.execute('UPDATE pet SET checked_in =%s WHERE id=%s',('FALSE',id))
    return ('OK', 200)

  elif request.method == 'DELETE':
    print(id)
    cur.execute('DELETE from pet WHERE pet.id=%s',(id,))
    return('OK', 200)
  
# @app.route('/owner', methods=['GET', 'POST', 'DELETE'])



  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'

