import os.path
import sqlite3

database = './goose.db'
checkDB = os.path.isfile(database)
conn = sqlite3.connect("goose.db")
cursor = conn.cursor()

#if DB does not exist create it
def initDB():
    if checkDB == False:
        for sql in runsql('create.sql'):
            cursor.execute(sql)

def sqlFileToStringArray(fname):
    with open('./SQL/' + fname, 'r') as file:
        sql = file.read()
    sqlArray = sql.split(2*os.linesep)
    return sqlArray

def multiSelect(fName):
    multiSelectArray = []
    for query in sqlFileToStringArray(fName):
        cursor.execute(query)
        multiSelectArray.append(cursor.fetchone())
    return multiSelectArray