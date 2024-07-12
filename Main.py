import os.path
import sqlite3

database = './goose.db'

checkDB = os.path.isfile(database)

conn = sqlite3.connect("goose.db")
cursor = conn.cursor()

if checkDB == False:
    with open('./SQL/create.sql', 'r') as file:
        sql = file.read()
    cursor.execute(sql)
