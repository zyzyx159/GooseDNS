from beaupy import confirm, select
from rich.console import Console
from DBInterface import *
import pandas as pd

DBInterface().create()

console = Console()

report = DBInterface().reportShort()

console.print('You have ' + report[0] + ' Domains registered, ' + report[1] + ' of which are active.')
console.print('You have ' + report[2] + ' Subdomains registered, ' + report[3] + ' of which are active.')
console.print('')

selOptions = [
    'Register a new domain',
    'Edit existing domain',
    'Register a new subdomain',
    'Edit and existing subdomain'
]

con = sqlite3.connect("goose.db")

opt = select(selOptions, cursor="🢧", cursor_style="cyan")

#I wanted to use a switch statement, but in Python the match option does not work that way.
if opt == selOptions[0]:
    console.print('new domain')
elif opt == selOptions[1]:
    drawDomainTable()
elif opt == selOptions[2]:
    console.print('new subdomain')
elif opt == selOptions[3]:
    df = pd.read_sql_query('select * from Subdomains', con)
    print(df.to_markdown(index=False, tablefmt='grid'))
else:
    console.print('This should not be possible')
    
def drawDomainTable():
    df = pd.read_sql_query('select * from domain', con)
    print(df.to_markdown(index=False, tablefmt='grid'))
    con.close()