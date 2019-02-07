import sqlite3

conn = sqlite3.connect('da2.db')
conn.execute("CREATE TABLE un (name TEXT, age TEXT, email TEXT, teacher TEXT)")
conn.execute('CREATE TABLE users (fname TEXT, lname TEXT, email TEXT, uname TEXT, password TEXT)')
conn.close()
