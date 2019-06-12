import psycopg2

conn = psycopg2.connect(host="localhost",
                        database="pet_hotel"
                        )

cur = conn.cursor()
cur.execute('SELECT * FROM pet')
# for record in cur:
#     print(record)
rows = cur.fetchall()
print(rows)

# cur.execute(
#     "CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")


conn.commit()
