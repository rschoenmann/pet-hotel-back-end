import psycopg2

conn = psycopg2.connect(host="localhost", database="pet_hotel")
                        

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

conn.commit()
