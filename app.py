import psycopg2

conn = psycopg2.connect(host="localhost",
                        database="pet_hotel"


                        )

cur = conn.cursor()
from flask import Flask
app = Flask(__name__)

@app.route('/test')
def test_get():
  cur.execute(
      "SELECT * FROM pet;")
  rows = cur.fetchall()
  print(rows)
  # tupleRows = tuple(rows)
  return(rows)

@app.route('/greet')
def say_hello():
  return 'Hello from Server'


conn.commit()
