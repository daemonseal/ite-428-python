#!\xampp\htdocs\python-service-request\venv\Scripts\python.exe
import myDatabase
import json

print("Content-type:text/html; charset=utf-8\n")

db = myDatabase.connectdb()
cursor = db.cursor()
sql_command = 'select * from products'
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
