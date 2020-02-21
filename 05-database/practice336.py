import sqlite3

def showReport(db, start_price, end_price, sort):
   params = (start_price, end_price)
   try:
       with (sqlite3.connect(db)) as conn:
           conn.row_factory = sqlite3.Row
           sql_command ="""
           select productname, unitprice from products
           where unitprice between ? and ?
           order by unitprice """ + sort
           cursor = conn.execute(sql_command, params)
           results_found = len(conn.execute(sql_command, params).fetchall())
           print("\nFound {} results.".format(results_found))
           for idx,i in enumerate(cursor):
               #print("{} - {} - {}".format(i[0],i[1],i[5]))
               print("{:>4}.) {:<40} : {:>10.2f} Baht".format
                     (idx+1,i["productname"],i["unitprice"]))
   except Exception as e:
       print("Error {}".format(e))


if __name__ == '__main__':
   myDatabase = "AppData/Sqlite_Northwind.sqlite3"
   while True:
      startPrice = int(input("Enter start price you want to see : "))
      endPrice = int(input("Enter end price you want to see : "))
      if endPrice > startPrice:
         break
      else:
         print(">>> End price should be more than start price.")
   while True:
      sortPrice = input("Sort price: [1] Ascending [2] Descending \nSelect [1] or [2] :")
      if sortPrice in ("1","2"):
         break
      else:
         print("Please enter the valid value.")

   sortPrice = "ASC" if sortPrice == "1" else "DESC"
   showReport(myDatabase, startPrice, endPrice, sortPrice)
