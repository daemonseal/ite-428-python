#!\xampp\htdocs\python-service-request\venv\Scripts\python.exe
import requests
import json
import cgi

print("Content-type:text/html; charset=utf-8\n")

form = cgi.FieldStorage()
unp = form.getvalue('unp')
sort = form.getvalue('sort')
desc = sort == 'desc'
param = {'unp': unp, 'sort': sort}
url = 'http://localhost/python-service-request/service3.py'
r = requests.get(url, params=param)
data = json.loads(r.content)

print('''<html>
<head>
    <title>request2</title>
</head>
<body>''')
print(f'''<form action="request2.py">
    <div><input type="text" placeholder="Min Price" name="unp" value="{unp or ''}" /></div>
    <div></div>
    <input type="radio" name="sort" value="asc" id="asc" {'checked' if not desc else ''} />
    <label for="asc">asc</label>
    <input type="radio" name="sort" value="desc" id="desc" {'checked' if desc else ''} />
    <label for="desc">desc</label>
    <div>
        <button class="button" type="submit">ok</button>
        <input class="button" type="button" onclick="window.location.href = 'request2.py';" value="reset"/>
    </div>
</form>''')

if data == 'no':
    print('not found.')
else:
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

print('</body></html>')
