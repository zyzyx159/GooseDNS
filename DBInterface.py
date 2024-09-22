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

    def readSQL(self, file):
        with open('./SQL/' + file + '.sql', 'r') as file:
            sql = file.read()
        sqlArray = sql.split(2*os.linesep)
        return sqlArray
