import os.path
import sqlite3

class SQLHandler(object):
    database = './goose.db'
    checkDB = os.path.isfile(database)
    conn = sqlite3.connect("goose.db")
    cursor = conn.cursor()
    
    def __init__(self, fName):
        self.DBCheck
        self.fName = fName
        #print(self.database)

    def DBCheck(self):
        if checkDB == False:
            for sql in runsql('create.sql'):
                cursor.execute(sql)

    def sqlFileToStringArray(self):
        with open('./SQL/' + self.fName, 'r') as file:
            sql = file.read()
        sqlArray = sql.split(2*os.linesep)
        return sqlArray

    def singleSelect(self):
        for sql in runSQL(self.fName):
            cursor.execute(sql)
        return 

    def multiSelect(self):
        multiSelectArray = []
        for query in self.sqlFileToStringArray():
            self.cursor.execute(query)
            multiSelectArray.append(self.intConvertTuple(self.cursor.fetchone()))
        return multiSelectArray

    def intConvertTuple(self, tup):
        string = ''.join(map(str, tup))
        return string

    def strConvertTuple(self, tup):
        string = ''.join(tup)
        return string

