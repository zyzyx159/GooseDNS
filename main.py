from beaupy import confirm, select
from rich.console import Console
from DBInterface import *
from dataFrame import *
import pandas as pd
import os

DBInterface().create()

console = Console()

dataFrame().report()

selOptions = [
    'Domains',
    'Subdomains',
    'Core settings'
]

opt = select(selOptions, cursor="🢧", cursor_style="cyan")

#I wanted to use a switch statement, but in Python the match option does not work that way.
if opt == selOptions[0]:
    dataFrame.drawTable('domain')
    command = input("Index to edit: ")
elif opt == selOptions[1]:
    dataFrame.drawTable('subdomains')
elif opt == selOptions[2]:
    console.print('Core options')
else:
    console.print('This should not be possible')