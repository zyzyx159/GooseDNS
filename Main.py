import os.path
import sqlite3

database = './goose.db'
checkDB = os.path.isfile(database)
conn = sqlite3.connect("goose.db")
cursor = conn.cursor()

def runsql(fname):
    with open('./SQL/' + fname, 'r') as file:
        sql = file.read()
    sqlArray = sql.split(2*os.linesep)
    return sqlArray

#if DB does not exist create it
if checkDB == False:
    for sql in runsql('create.sql'):
        cursor.execute(sql)

reportQueries = runsql('reportShort.sql')
cursor.execute(reportQueries[0])
domains = str(cursor.fetchone()[0])

cursor.execute(reportQueries[1])
activeDomains = str(cursor.fetchone()[0])

cursor.execute(reportQueries[2])
subdomains = str(cursor.fetchone()[0])

cursor.execute(reportQueries[3])
activeSubdomains = str(cursor.fetchone()[0])

print('You have ' + domains + ' Domains registered, ' + activeDomains + ' of which are active.')
print('You have ' + subdomains + ' Subdomains registered, ' + activeSubdomains + ' of which are active.')
print('')
print('Available options:')
print('1. Register a new domain')
print('2. Activate/deactivate a domain')
print('3. Register a new subdomain')
print('4. Activate/deactivate a subdomain')