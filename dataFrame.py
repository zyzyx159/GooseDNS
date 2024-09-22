import pandas as pd
import sqlite3 as sqlite3

class dataFrame(object):
    conn = sqlite3.connect("goose.db")

    @classmethod
    def report(self):
        df = pd.read_sql_query(self.readSQL('report'), self.conn)
        print(df.to_markdown(index=False, tablefmt='grid'))
        print('')
        #self.conn.close()

    @classmethod
    def drawTable(self, table):
        df = pd.read_sql_query('select * from ' + table, self.conn)
        print(df.to_markdown(index=False, tablefmt='grid'))
        print('')
        #self.conn.close()

    @classmethod
    def readSQL(self, file):
        with open('./SQL/' + file + '.sql', 'r') as file:
            sql = file.read()
        return sql

#pick which row to edit by row id
#display that in a data frame

#edit the data frame
    #show changes to data frame in real time

#update the data frame
    #add code for the PC to pick between update and insert
