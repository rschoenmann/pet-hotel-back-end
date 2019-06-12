import psycopg2

conn = psycopg2.connect(host="localhost",
                        database="pet_hotel"
                        
                        
                        )

cur = conn.cursor()

cur.execute(
    "CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
conn.commit()
