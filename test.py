import os.path

with open('./SQL/create.sql', 'r') as file:
    sql = file.read()
#cursor.execute(sql)
split = sql.split(';')

for sql in split:
    print(sql)
