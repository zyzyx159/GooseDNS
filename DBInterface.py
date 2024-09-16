import os.path
import sqlite3

class DBInterface(object):
    database = './goose.db'
    checkDB = os.path.isfile(database)
    conn = sqlite3.connect("goose.db")
    cursor = conn.cursor()

    def create(self):
        if self.checkDB == False: 
            sqlArray = self.readSQL("create")
            for query in sqlArray:
                self.cursor.execute(query)

    def domainSelect(self):
        #place holder
        #I will do things later
        print("later")

    def reportShort(self):
        ReportShortArray = []
        sqlArray = self.readSQL("reportShort")
        for query in sqlArray:
            self.cursor.execute(query)
            ReportShortArray.append(self.intConvertTuple(self.cursor.fetchone()))
        return ReportShortArray

    def readSQL(self, file):
        with open('./SQL/' + file + '.sql', 'r') as file:
            sql = file.read()
        sqlArray = sql.split(2*os.linesep)
        return sqlArray

    def intConvertTuple(self, tup):
        string = ''.join(map(str, tup))
        return string

    def strConvertTuple(self, tup):
        string = ''.join(tup)
        return string

