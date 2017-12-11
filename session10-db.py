import sqlite3

connection = sqlite3.connect("test_database.db")
cursor = connection.cursor()
# We create our first TABLE People that will
# store the field FirstName, LastName and Age

cursor.execute("INSERT INTO People "
               "VALUES ('Ron', 'Obvious', 42)")
# we have to commit to actually
# save the record in database
connection.commit()