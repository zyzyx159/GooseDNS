import os.path
import sqlite3
from beaupy import confirm, select
from rich.console import Console

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

selOptions = [
    'Register a new domain',
    'Edit existing domain',
    'Register a new subdomain',
    'Edit and existing subdomain'
]

console = Console()

console.print('You have ' + domains + ' Domains registered, ' + activeDomains + ' of which are active.')
console.print('You have ' + subdomains + ' Subdomains registered, ' + activeSubdomains + ' of which are active.')
console.print('')
opt = select(selOptions, cursor="🢧", cursor_style="cyan")
console.print("{opt}")