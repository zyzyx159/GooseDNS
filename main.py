from beaupy import confirm, select
from rich.console import Console
from sqlHandler import *

initDB()

selOptions = [
    'Register a new domain',
    'Edit existing domain',
    'Register a new subdomain',
    'Edit and existing subdomain'
]

console = Console()

report = multiSelect('reportShort.sql')

console.print('You have ' + str(report[0]) + ' Domains registered, ' + str(report[1]) + ' of which are active.')
console.print('You have ' + str(report[2]) + ' Subdomains registered, ' + str(report[3]) + ' of which are active.')
console.print('')
opt = select(selOptions, cursor="🢧", cursor_style="cyan")

#I wanted to use a switch statement, but Python the match option does not work that way.
if opt == selOptions[0]:
    console.print('new domain')
elif opt == selOptions[1]:
    console.print('edit domain')
elif opt == selOptions[2]:
    console.print('new subdomain')
elif opt == selOptions[3]:
    console.print('edit subdomain')
else:
    console.print('This should not be possible')