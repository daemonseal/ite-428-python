#!\xampp\htdocs\python-service-request\venv\Scripts\python.exe
import myDatabase
import json
import cgi

print("Content-type:text/html; charset=utf-8\n")

form = cgi.FieldStorage()
unp = form.getvalue('unp')
desc = form.getvalue('sort') == 'desc'

where = f' where UnitPrice >= {unp}' if unp else ''
order = f' order by UnitPrice {"desc" if desc else ""}'
sql_command = f'''select * from products{where}{order};'''

db = myDatabase.connectdb()
cursor = db.cursor()
cursor.execute(sql_command)
rows = cursor.fetchall()

if rows:
    result = []
    for i in rows:
        data = {
            "id": f'{i["ProductID"]}',
            "name": f'{i["ProductName"]}',
            "price": f'{i["UnitPrice"]}',
        }
        result.append(data)
    print(json.dumps(result))
else:
    print(json.dumps('no'))
