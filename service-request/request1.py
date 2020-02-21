#!\xampp\htdocs\python-service-request\venv\Scripts\python.exe
import requests
import json
import cgi

print("Content-type:text/html; charset=utf-8\n")

form = cgi.FieldStorage()
prodID = form.getvalue('prodID')
param = { 'id': prodID }
url = 'http://localhost/python-service-request/service2.py'
r = requests.get(url, params=param)
data = json.loads(r.content)

print('''<html>
<head>
    <title>request1</title>
    <link href="https://fonts.googleapis.com/css?family=Noto+Sans&display=swap" rel="stylesheet">
</head>
<body>''')
print(f'''<form action="request1.py">
    <input type="text" placeholder="id" name="prodID" value="{prodID or ''}" />
    <button class="button" type="submit">ok</button>
    <input class="button" type="button" onclick="window.location.href = 'request1.py';" value="reset"/>
</form>''')

if data:
    print('<table>')
    print('''
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Price</td>
        </tr>
    ''')
    [print(f'''
        <tr>
            <td>{d['id']}</td>
            <td>{d['name']}</td>
            <td>{d['price']}</td>
        </tr>
    ''') for d in data]
    print('</table>')
else:
    print('not found.')


print('</body></html>')
