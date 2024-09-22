import pandas as pd
import sqlite3 as sqlite3

#do data frame stuff
class dataFrame(object):
    con = sqlite3.connect("goose.db")

#select * from <table> into a data frame
#print said data frame
#should not be pulling its own data, that's what the DB interface is for
    def drawTable(table):
        con = sqlite3.connect("goose.db") #why does the above con not work?
        df = pd.read_sql_query('select * from ' + table, con)
        print(df.to_markdown(index=False, tablefmt='grid'))
        con.close()

#pick which row to edit by row id
#display that in a data frame

#edit the data frame
    #show changes to data frame in real time

#update the data frame
    #add code for the PC to pick between update and insert
