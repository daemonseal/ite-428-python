import csv
import sqlite3
from datetime import datetime


def genReportList():
    """
    Generate a list of reports and their information
    """
    reportList = [{
        'description': 'Show products by price range',
        'show_function': showProductByPriceRange,
        'sql_command': """ select productname, unitprice from products
            where unitprice between ? and ? order by unitprice """,
        'ask_function': askProductByPriceRange,
        'is_sorted': True,
        'print_results_found': True
    }, {
        'description':
        'Show products by category ',
        'ask_function':
        askProductByCategory,
        'show_function':
        showProductByCategory,
        'sql_command':
        """
            select ProductName, UnitPrice
            from Products p join Categories c
            on p.CategoryId = c.CategoryId
            where lower(CategoryName) = ?
            order by 1
            """,
    }, {
        'description':
        'Show supplies in each country',
        'show_function':
        showSuppliersGroupByCountry,
        'sql_command':
        """
            select Country, count(SupplierId) as 'No. of Company'
            from Suppliers group by Country order by 2 DESC;
            """,
    }, {
        'description':
        'Show customers by region',
        'show_function':
        showCustomersByRegion,
        'sql_command':
        """
            select region, count(distinct country) country, count(distinct city) city
            from customers
            group by region
            order by 3 desc;
            """,
    }, {
        'description':
        'Show stock value product',
        'ask_function':
        askProductStockValue,
        'show_function':
        showProductStockValue,
        'sql_command':
        """
            select productid, productname, unitprice * unitsinstock as stockvalue
            from products
            where stockvalue > ?
            order by stockvalue desc;
            """,
    }, {
        'description': 'Show value of stock by category',
        'ask_function': askStockValueByCategory,
        'show_function': showStockValueByCategory,
        'sql_command': """
            select c.categoryname, count(p.productid) pd, sum(p.unitprice * p.unitsinstock) value
            from categories c join products p on c.categoryid = p.categoryid
            group by c.categoryname
            having value > ?
            order by 3;
            """,
        'print_results_found': True
    }, {
        'description':
        'Show employees and orders they manage',
        'show_function':
        showEmployeesAndOrders,
        'sql_command':
        """ select e.FirstName || ' '
            || e.LastName || ' , ' || e.TitleOfCourtesy as
            emp_name, count(o.OrderId) all_orders from Employees e join
            Orders o on e.EmployeeId = o.EmployeeId group by emp_name order
            by all_orders; """,
    }, {
        'description':
        'Show suppliers and their categorized product details',
        'show_function':
        showProductAndAvgPriceBySuppliersAndCategory,
        'sql_command':
        """
            select s.companyname, c.categoryname,
            count(p.productid) pd, avg(p.unitprice) avg_price
            from products p
            join categories c on p.categoryid = c.categoryid
            join suppliers s on p.supplierid = s.supplierid
            group by 1, 2;
            """,
    }, {
        'description':
        'Show an invoice of a specific order',
        'ask_function':
        askInvoice,
        'show_function':
        showInvoice,
        'sql_command':
        """
            select o.OrderId, o.OrderDate, c.CompanyName customer, p.ProductName,
            d.UnitPrice * d.Quantity as price, s.CompanyName shipper
            from Orders o
            join Products p on p.ProductId = d.ProductId
            join Customers c on o.CustomerId = c.CustomerId
            join OrdersDetails d on o.OrderId = d.OrderId
            join Shippers s on o.ShipVia = s.ShipperID
            where o.OrderId = ?
            order by p.ProductName ASC;
             """,
    }, {
        'description':
        'Show customer by sales',
        'show_function':
        showCustomersBySales,
        'sql_command':
        """
            select c.Country country, count(o.OrderId) number,
            sum(d.UnitPrice * d.Quantity) price, avg(d.UnitPrice * d.Quantity) po
            from Orders o
            join Customers c on o.CustomerId = c.CustomerId
            join OrdersDetails d on o.OrderId = d.OrderId
            group by country
            order by po DESC;
            """,
    }]
    return reportList


def genCommandList():
    """
    Generate a list of commands for database managemennt
    """
    commandList = [
        {
            'description': 'Add new category',
            'function': addNewCategory
        },
        {
            'description': 'Change contact suppliers',
            'function': changeContactSupplier,
        },
        {
            'description': 'Delete order id',
            'function': deleteOrder,
        },
        {
            'description': 'Create a new table called student',
            'function': createStudentTable
        },
    ]
    return commandList


def printLine(c='-', n=50):
    print(c * n)


def showReport(db, reportType):
    try:
        with (sqlite3.connect(db)) as conn:
            conn.row_factory = sqlite3.Row
            sql_command = reportType['sql_command']
            if reportType.get('is_sorted', False):
                sql_command = '{} {}'.format(sql_command,
                                             reportType['sort_mode'])
            params = reportType.get('params', None)
            if params is not None:
                sql_args = (sql_command, params)
            else:
                sql_args = (sql_command, )
            cursor = conn.execute(*sql_args)
            if reportType.get('print_results_found', False):
                results_found = len(conn.execute(*sql_args).fetchall())
                reportType['show_function'](cursor, results_found)
            else:
                reportType['show_function'](cursor)
    except sqlite3.DatabaseError as e:
        print("Error {}".format(e))


def askProductByPriceRange():
    while True:
        startPrice = int(input("Enter start price you want to see : "))
        endPrice = int(input("Enter end price you want to see : "))
        if endPrice > startPrice:
            break
        else:
            print("End price should be more than start price.")
    while True:
        sortPrice = input(
            "Sort price: [1] Ascending [2] Descending \nSelect [1] or [2] :")
        if sortPrice in ("1", "2"):
            break
        else:
            print("Please enter the valid value.")
    sortPrice = "ASC" if sortPrice == "1" else "DESC"
    params = (startPrice, endPrice)
    return params, sortPrice


def showProductByPriceRange(cursor, results_found):
    print('Found {} record(s).'.format(results_found))
    for idx, i in enumerate(cursor):
        print("{:>4}.) {:<40} : {:>10.2f} Baht".format(idx + 1,
                                                       i["productname"],
                                                       i["unitprice"]))


def askProductByCategory():
    category = input("Enter the category type you want to see : ")
    return (category.lower(), )


def showProductByCategory(cursor):
    for idx, i in enumerate(cursor):
        print("{:>4}.) {:<40} : {:>10.2f} Baht".format(idx + 1,
                                                       i["productname"],
                                                       i["unitprice"]))


def showSuppliersGroupByCountry(cursor):
    print('{:<30} {:>4}'.format('Suppliers From', 'No. of Company'))
    for idx, i in enumerate(cursor):
        print("{:<30} {:>4}".format(i["country"], i["No. of Company"]))


def showCustomersByRegion(cursor):
    print('Show customers by region')
    printLine()
    print('{:<30} {:>8} {:>8}'.format('Region', 'Country', 'City'))
    printLine()
    for i in cursor:
        print('{:<30} {:>8} {:>8}'.format(i['Region'], i['Country'],
                                          i['City']))


def askProductStockValue():
    value = int(input("Please enter minimum stock value you want to see : "))
    return (value, )


def showProductStockValue(cursor):
    output_format = """\
      ID = {}
      PRODUCT NAME = {}
      STOCK VALUE = {:,.2f} """
    for i in cursor:
        print(
            output_format.format(i['productid'], i['productname'],
                                 i['stockvalue']))
        printLine()


def askStockValueByCategory():
    value = int(
        input(
            "Please enter minimum stock value you want to see (Group by category): "
        ))
    return (value, )


def showStockValueByCategory(cursor, results_found):
    print('Found {} category(s).'.format(results_found))
    for idx, i in enumerate(cursor):
        print("{:>4}.) {:<20} {:<4} PD. {:>10.2f} Baht".format(
            idx + 1, i["categoryname"], i["pd"], i["value"]))


def showEmployeesAndOrders(cursor):
    for idx, i in enumerate(cursor):
        print("{:>4}.) {:<30} {:>10}".format(idx + 1, i["emp_name"].upper(),
                                             i["all_orders"]))


def showProductAndAvgPriceBySuppliersAndCategory(cursor):
    for i in cursor:
        print("{} ({}) No. of Product = {} (Average price = {:,.2f})".format(
            i['companyname'], i["categoryname"], i["pd"], i["avg_price"]))


def askInvoice():
    search_for_id = input('Please enter Order ID : ')
    return (search_for_id, )


def showInvoice(cursor):
    # define format
    header_format = "{:<10} : {}\n{:<10} : {}\n{:<10} : {}"
    product_format = "{}.) {:<48} {:>10,.2f}"
    total_format = "{:>50} : {:>10,.2f}\n{:>50} : {:>10,.2f}\n{:>50} : {:>10,.2f}"
    sendby_format = "Send By : {}"
    # placeholders
    orderId = ''
    total = 0
    send_by = ""
    for idx, i in enumerate(cursor):
        if idx == 0:
            orderId = i['orderid']
            orderDate = i['orderdate']
            print(
                header_format.format('Order ID', i['orderid'], 'Order Date',
                                     i['orderdate'], 'Customer',
                                     i['customer']))
            printLine(n=70)
            send_by = i['shipper']
        print(product_format.format(idx + 1, i['productname'], i['price']))
        total += i['price']
    printLine(n=70)
    # calculate net price
    vat = total * 0.07
    net_price = total + vat
    print(
        total_format.format('TOTAL PRICE', total, 'VAT (7%)', vat, 'NET PRICE',
                            net_price))
    printLine(n=70)
    print(sendby_format.format(send_by))

    dateTime = datetime.now().strftime('%Y/%m/%d, %H:%M:%S')
    output = orderId, net_price, dateTime
    print(output)

    # write to csv
    with open('AppData/orderinfo.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(output)
    print('Log is written to AppData/orderinfo.csv')


def showCustomersBySales(cursor):
    print('Show customers by sales')
    printLine(n=70)
    header_format = "{:<20} {:>5} {:>15} {:>20}"
    result_format = "{:<20} {:>5} {:>20,.2f} {:>20,.2f}"
    print(
        header_format.format('Country', 'No.Of Order', 'NET Price',
                             'Price/Order'))
    printLine(n=70)
    for i in cursor:
        print(
            result_format.format(i['country'], i['number'], i['price'],
                                 i['po']))


def addNewCategory(db):
    category = input("Please input new category to add : ")
    description = input("Please input description : ")
    try:
        with sqlite3.connect(db) as conn:
            sql_command = """
            INSERT INTO Categories(CategoryName, Description)
            VALUES (?, ?);
            """
            conn.execute(sql_command, (category, description))
            # conn.executescript(sql_command, params)
            # USE THIS IF YOU USE MULTIPLE COMMANDS e.g. COMMIT;
            # sqlite will auto commit when we close the database
            print('New category was added!')
    except sqlite3.DatabaseError as e:
        print('Error while connecting to the database', e)


def changeContactSupplier(db):
    supplier_id = input("Please input supplier id : ")
    try:
        with sqlite3.connect(db) as conn:
            sql_command = """
            SELECT ContactName from Suppliers
            where SupplierId = ?;
            """
            cursor = conn.execute(sql_command, supplier_id)
            print(*cursor.fetchone())
            # conn.executescript(sql_command, params)
            # USE THIS IF YOU USE MULTIPLE COMMANDS e.g. COMMIT;
            # sqlite will auto commit when we close the database
    except sqlite3.DatabaseError as e:
        print('Error while connecting to the database', e)

    choice = input('Do you want to change contact name? (Y/n)').lower()
    if choice == 'y':
        params = input("Please input the contact name : ")
        try:
            with sqlite3.connect(db) as conn:
                sql_command = """
                UPDATE Suppliers
                SET ContactName = ?
                WHERE SupplierId = id
                """
                conn.execute(sql_command, params)
                print('ContactName was updated!')
        except sqlite3.DatabaseError as e:
            print('Error while connecting to the database', e)


def deleteOrder(db):
    order_id = input('Please input order ID : ')
    try:
        with sqlite3.connect(db) as conn:
            conn.row_factory = sqlite3.Row
            sql_command = """
            select orderid, customerid, orderdate, requireddate, shippeddate
            from orders where orderid = ?;
            """
            cursor = conn.execute(sql_command, (order_id,))
            # conn.executescript(sql_command, params)
            # USE THIS IF YOU USE MULTIPLE COMMANDS e.g. COMMIT;
            # sqlite will auto commit when we close the database
            output = """
            OrderID = {}
            CustomerID = {}
            OrderDate = {}
            RequiredDate = {}
            ShippedDate = {}
            """
            for r in cursor:
                print(
                    output.format(r['orderid'], r['customerid'],
                                  r['orderdate'], r['requireddate'],
                                  r['shippeddate']))

    except sqlite3.DatabaseError as e:
        print('Error while connecting to the database', e)

    choice = input('Do you want to delete this order? (y/N) : ').lower()
    if choice == 'y':
        try:
            with sqlite3.connect(db) as conn:
                sql_command = """
                DELETE FROM OrdersDetails where OrderId = {};
                DELETE FROM Orders where OrderId = {};
                """.format(order_id, order_id)
                order = conn.executescript(sql_command)
                print('Order deleted!')
        except sqlite3.DatabaseError as e:
            print('Error while connecting to the database', e)


def createStudentTable(db):
    try:
        with sqlite3.connect(db) as conn:
            sql_command = """
            CREATE TABLE "Students" (
                "ID"	INTEGER,
                "NAME"	TEXT NOT NULL,
                "LASTNAME"	TEXT NOT NULL,
                "GENDER"	TEXT NOT NULL,
                PRIMARY KEY("ID")
            )
            """
            conn.execute(sql_command)
            print("Created a table called student in {}.".format(db))
    except sqlite3.DatabaseError as e:
        print(e)


def main():
    print("Enter 1 to query reports\nEnter 2 to manage database")
    mode = input("What do you want to do ? ")
    if mode == '1':
        # Ask users what kind of report they want to see
        print("What kind of report do you want to see?")
        # Loop until users input valid value
        while True:
            for i, r in enumerate(reportList):
                print('[{}] {}'.format(i + 1, r['description']))
            choice = int(input("Please choose your report type : "))
            if choice in range(1, 11):
                break
            else:
                print(
                    "\nPlease choose a valid report type using numbers e.g. 1, 2, 3"
                )

        # Report functions
        # Using choice - 1 because reportList index starts from 0
        reportType = reportList[choice - 1]
        # Check whether the report need params
        params = reportType.get('ask_function', None)
        if params is not None:
            if reportType.get('is_sorted', False):
                # Kinda dirty here, but some report also need sort_mode
                reportType['params'], reportType['sort_mode'] = params()
            else:
                reportType['params'] = params()

        # showReport() is the only function that connect to the database
        # the rest (asking for users input, format and output the results)
        # are handled by other functions specific to each reportType
        showReport(myDatabase, reportType)
    elif mode == '2':
        print("Database management...")
        # Loop until users input valid value
        while True:
            for i, r in enumerate(commandList):
                print('[{}] {}'.format(i + 1, r['description']))
            choice = int(input("What do you want to do ? "))
            if choice in range(1, 5):
                break
            else:
                print(
                    "\nPlease choose a valid command type using numbers e.g. 1, 2, 3"
                )

        # run database management function
        print(commandList[choice - 1]['description'])
        commandList[choice - 1]['function'](myDatabase)


if __name__ == '__main__':
    # Define a list of dictionary that contains
    # different report types and their metadata
    # Using list because it is ordered and
    # I want to loop through all the description
    reportList = genReportList()
    commandList = genCommandList()

    # Define database file path
    myDatabase = "AppData/Sqlite_Northwind.sqlite3"

    main()
