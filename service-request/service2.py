#!\xampp\htdocs\python-service-request\venv\Scripts\python.exe
import myDatabase
import json
import cgi

print("Content-type:text/html; charset=utf-8\n")

form = cgi.FieldStorage()
inputID = form.getvalue('id')

db = myDatabase.connectdb()
cursor = db.cursor()
sql_command = f'select * from products where ProductID="{inputID}"' if inputID else 'select * from products'
cursor.execute(sql_command)
rows = cursor.fetchall()
result = []
for i in rows:
    data = {
        "id": f'{i["ProductID"]}',
        "name": f'{i["ProductName"]}',
        "price": f'{i["UnitPrice"]}',
    }
    result.append(data)

print(json.dumps(result))
