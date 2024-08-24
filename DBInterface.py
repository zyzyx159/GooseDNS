import os.path
import sqlite3

class DBInterface(object):
    database = './goose.db'
    checkDB = os.path.isfile(database)
    conn = sqlite3.connect("goose.db")
    cursor = conn.cursor()

    def create(self):
        if checkDB == False:
            for sql in runsql('create.sql'):
                cursor.execute(sql)

    def domainSelect(self):
        #place holder
        #I will do things later
        print("later")

    def reportShort(self):
        ReportShortArray = []
        with open('./SQL/reportShort.sql', 'r') as file:
            sql = file.read()
        sqlArray = sql.split(2*os.linesep)
        for query in sqlArray:
            self.cursor.execute(query)
            ReportShortArray.append(self.intConvertTuple(self.cursor.fetchone()))
        return ReportShortArray

    def intConvertTuple(self, tup):
        string = ''.join(map(str, tup))
        return string

    def strConvertTuple(self, tup):
        string = ''.join(tup)
        return string

