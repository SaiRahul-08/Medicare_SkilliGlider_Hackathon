import sqlite3

connection = sqlite3.connect('database.db')

with open('database/schema.sql', 'r') as file:
    schema = file.read()

connection.executescript(schema)

connection.commit()
connection.close()

print("Database and tables created successfully.")