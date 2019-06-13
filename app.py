import psycopg2
from flask import Flask, jsonify, request
# app.debug = True

app = Flask(__name__)

conn = psycopg2.connect(host="localhost",
                        database="pet_hotel"
                        )

cur = conn.cursor()
conn.set_session(autocommit=True)

cur.execute('SELECT * FROM pet')
cur.fetchone()

@app.route('/pet', methods=['GET', 'POST', 'PUT', 'DELETE'])
def petRoutes():
  if request.method == 'GET':
	  cur.execute('SELECT * FROM pet JOIN owner ON owner.id=pet.owner_id')
	  rows = jsonify(cur.fetchall())
	  print(rows)
	  return rows
    

  elif request.method == 'POST':
    cur.execute('INSERT INTO pet (pet_name, owner_id, breed, color) VALUES(%s,%s,%s,%s)',('fluffy',1,'cotton mouth','black'))
    print('hey')
    return 'OK',200

  
# @app.route('/owner', methods=['GET', 'POST', 'DELETE'])
cur.execute('SELECT * FROM pet')
rows = cur.fetchall()
print(rows)


  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'


# Make the changes to the database persistent
conn.commit()


