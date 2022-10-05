import psycopg2


# connect to 'chinook' database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database which is like the arrays we retrieve
cursor = connection.cursor()

# TO PERFORM QUERIES LAST STEP
# Query 1 - select all records from the Artist table With single quotes
# run the query created with set_pg python3 sql-psycopg2.py
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only Name collumn from the Artist table With single quotes
# run the query crrated with python3 sql-psycopg2.py
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only queen records from the Artist table With single quotes
# run the query crrated with python3 sql-psycopg2.py
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from "Artist" table
# run the query crrated with python3 sql-psycopg2.py
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only the albums with "ArtistId" #51  on the "Album" table
# run the query crrated with python3 sql-psycopg2.py
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all tracks where the composer is queen from track table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])
# fetch the result for the cursor \\ use fetch for 1 rcord, fetchall for
# multiple

results = cursor.fetchall()

# fetchone example
# results = cursor.fetchone()

# close and end the connection to the database

connection.close()

# for retrieve the records from the cursor we created

# print results

for result in results:
    print(result)
