import psycopg2

# connwct to 'chinook' database

connection = psycopg2.connect(database="chinook")

# build a cursor object of the database which is like the arrays we retrieve

cursor = connection.cursor()

# TO PERFORM QUERIES LAST STEP
# Query 1 - select all records from the Artist table With single quotes
# run the query crrated with python3 sql-psycopg2.py
# REMOVE cursor.execute('Select * FROM "Artist"')

# Query 2 - select only Name collumn from the Artist table With single quotes
# run the query crrated with python3 sql-psycopg2.py
# REMOVE cursor.execute('Select "Name" FROM "Artist"')

# Query 3 - select only queen records from the Artist table With single quotes
# run the query crrated with python3 sql-psycopg2.py
# REMOVE cursor.execute('Select * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 3 - select only ArtistId  #51 from Artist table

# run the query crrated with python3 sql-psycopg2.py
cursor.execute('Select * FROM "Artist" WHERE "ArtistId" = %s', [51])

# fetch the result for the cursor
# use fetch for 1 rcord, fetchall for multiple

# results = cursor.fetchall()
# fetchone example
results = cursor.fetchone()
# close and end the connection to the database

connection.close()


# for retrieve the records from the cursor we created

# print results

for result in results:
    print(result)