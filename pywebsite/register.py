#!\xampp\htdocs\mywebsite\venv\Scripts\python
print("Context-type:text/html\n")
import sqlite3
import hashlib
import cgi
from datetime import date

form = cgi.FieldStorage()
usr = form.getvalue("username")
pwd = form.getvalue("password")
name = form.getvalue("name")
lastname = form.getvalue("lastname")
registerdate = date.today().strftime('%m/%d/%y')

usr = 'test2'
pwd = 'test'
name = 'test'
lastname = 'test'

pwd_encode = hashlib.md5(pwd.encode()).hexdigest()

def connect_to_db(db_path):
    with sqlite3.connect(db_path) as conn:
        return conn


def get_user_data(conn, user):
    conn.row_factory = sqlite3.Row
    sql_command = """
    SELECT username, password, name, lastname 
    FROM users WHERE username = ? 
    """
    try:
        cursor = conn.execute(sql_command, (user,))
        return cursor
    except sqlite3.DatabaseError as e:
        print('Error: {}'.format(e))

def add_user_data(conn, data):
    sql_command = """
    INSERT INTO users VALUES (?, ?, ?, ?, ?)
    """
    try:
        conn.execute(sql_command, data)
        return True
    except sqlite3.DatabaseError as e:
        print("{}".format(e))
        return False


db_connection = connect_to_db("database/practice.sqlite3")
usr_data = get_user_data(db_connection, usr)

title = "Create new account"

print("<html>")
print("<head><title>{}</title></head>".format(title))
print("<body>")

result = list(usr_data)
data_to_insert = (usr, pwd_encode, name, lastname, registerdate)

if len(result) != 0:
    print("Username '{}' is already exist.".format(usr))
else:
    if add_user_data(db_connection, data_to_insert):
        print("Thank you for registering a new account, {}".format(usr))
    else:
        print("Error occur while registering you account.")

print("</body>")
print("</html>")
