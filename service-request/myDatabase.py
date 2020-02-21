#!\xampp\htdocs\python-service-request\venv\Scripts\python.exe
import pymysql

def connectdb():
    myDB = pymysql.connect(
        host = "localhost",
        port=3306,
        user = "root",
        passwd = "",
        cursorclass=pymysql.cursors.DictCursor,
        database = "northwind"
    )
    return myDB
