import sqlite3


def changeContactSupplier(db, supplier_id):
    try:
        with sqlite3.connect(db) as conn:
            sql_command = """
            SELECT ContactName from Suppliers
            where SupplierId = ?
            """
            cursor = conn.execute(sql_command, supplier_id)
            # conn.executescript(sql_command, params)
            # USE THIS IF YOU USE MULTIPLE COMMANDS e.g. COMMIT;
            # sqlite will auto commit when we close the database
            print(list(cursor)[0][0])
    except sqlite3.DatabaseError as e:
        print('Error while connecting to the database', e)

    choice = input('Do you want to change contact name? (y/N) : ').lower()
    if choice == 'y':
        new_contactname = input('Please enter the new contact name : ')
        try:
            with sqlite3.connect(db) as conn:
                sql_command = """
                UPDATE Suppliers
                SET ContactName = ?
                WHERE SupplierId = ?
                """
                conn.execute(sql_command, (new_contactname, supplier_id))
                print('ContactName was updated!')
        except sqlite3.DatabaseError as e:
            print('Error while connecting to the database', e)


if __name__ == '__main__':

    myDatabase = 'AppData/Sqlite_Northwind.sqlite3'

    supplier_id = input('Please input supplierid : ')
    changeContactSupplier(myDatabase, supplier_id)
