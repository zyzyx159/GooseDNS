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

    #def domainSelect(self):
        

    def maxDomainID(self):
        self.cursor.execute(self.readSQL('maxDomainID'))
        return int(self.intConvertTuple(self.cursor.fetchone()))

    def reportShort(self):
        ReportShortArray = []
        sqlArray = self.readSQL('reportShort')
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
        return ''.join(map(str, tup))

    def strConvertTuple(self, tup):
        return ''.join(tup)