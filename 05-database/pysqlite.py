import sqlite3
def showReport(db):
   try:
       with (sqlite3.connect(db)) as conn:
           conn.row_factory = sqlite3.Row
           sql_command ="select * from products;"
           cursor = conn.execute(sql_command)
           for i in cursor:
               #print("{} -  {} - {}".format(i[0],i[1],i[5]))
               print("{} -  {} - {}".format
                     (i["productid"],i["productname"],i["unitprice"]))
   except Exception as e:
       print("Error {}".format(e))


if __name__ == '__main__':
   myDatabase = "Appdata/Sqlite_Northwind.sqlite3"
   showReport(myDatabase)
