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
        

    def maxDomainID(self):
        self.cursor.execute(self._readFile('maxDomainID.sql'))
        return int(self.intConvertTuple(self.cursor.fetchone()))

    def reportShort(self):
        ReportShortArray = []
        sqlArray = self._readFile('reportShort.sql').split(2*os.linesep)
        for query in sqlArray:
            self.cursor.execute(query)
            ReportShortArray.append(self.intConvertTuple(self.cursor.fetchone()))
        return ReportShortArray

    def _readFile(self, fileName):
        with open('./SQL/' + fileName, 'r') as file:
            sql = file.read()
        return sql

    def intConvertTuple(self, tup):
        return ''.join(map(str, tup))

    def strConvertTuple(self, tup):
        return ''.join(tup)