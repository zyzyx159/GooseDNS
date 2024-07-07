import os.path
import sqlite3

database = './goose.db'

checkDB = os.path.isfile(database)

conn = sqlite3.connect("goose.db")
cursor = conn.cursor()
# cursor.execute(create_table_sql)
print(checkDB)