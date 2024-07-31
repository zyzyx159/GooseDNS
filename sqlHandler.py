import os.path
import sqlite3

database = './goose.db'
checkDB = os.path.isfile(database)
conn = sqlite3.connect("goose.db")
cursor = conn.cursor()

def initDB():
    if checkDB == False:
        for sql in runsql('create.sql'):
            cursor.execute(sql)

def sqlFileToStringArray(fName):
    with open('./SQL/' + fName, 'r') as file:
        sql = file.read()
    sqlArray = sql.split(2*os.linesep)
    return sqlArray

def singleSelect(fName):
    for sql in runSQL(fName):
        cursor.execute(sql)
        
    return 

def multiSelect(fName):
    multiSelectArray = []
    for query in sqlFileToStringArray(fName):
        cursor.execute(query)
        multiSelectArray.append(intConvertTuple(cursor.fetchone()))
    return multiSelectArray

def intConvertTuple(tup):
    string = ''.join(map(str, tup))
    return string

def strConvertTuple(tup):
    string = ''.join(tup)
    return string

