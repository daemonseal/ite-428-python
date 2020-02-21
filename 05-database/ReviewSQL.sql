-- 1
select ProductName, UnitPrice, UnitsInStock from Products;

-- 2
select ProductName, UnitPrice as Price, UnitsInStock from Products;

-- 3
select ProductName, UnitPrice as Price, UnitsInStock, (UnitPrice * UnitsInStock) ValueInStock from Products;

-- 4
select upper(ProductName) as Product, UnitPrice Price, UnitsInStock, (UnitPrice * UnitsInStock) ValueInStock from Products;

-- 5
select upper(ProductName) as Product, UnitPrice Price, UnitsInStock, (UnitPrice * UnitsInStock) ValueInStock 
from Products
order by 4 desc;

-- 6
select upper(ProductName) as Product, UnitPrice Price, UnitsInStock, (UnitPrice * UnitsInStock) ValueInStock 
from Products
where ValueInStock >= 3000
order by 4 desc;

-- 7
select upper(ProductName) as Product, UnitPrice Price, UnitsInStock, (UnitPrice * UnitsInStock) ValueInStock 
from Products
where Price < 100 and ValueInStock >= 3000
order by 4 desc;

-- 8
select upper(ProductName) as Product, UnitPrice Price, UnitsInStock, (UnitPrice * UnitsInStock) ValueInStock 
from Products
where UnitsInStock in (0, 10, 20)
order by UnitsInStock desc, Product;

-- 9
select upper(ProductName) as Product, UnitPrice Price, UnitsInStock, (UnitPrice * UnitsInStock) ValueInStock 
from Products
where UnitsInStock between 10 and 20
order by UnitsInStock desc, Product;

-- 10
select CompanyName, ContactName, Country, City, Fax
from Suppliers;

-- 11
select CompanyName, ContactName, Country, City, Fax
from Suppliers
where Country = 'USA';

-- 12
select CompanyName, ContactName, Country, City, Fax
from Suppliers
where Country = 'USA' and Fax is NULL;

-- 13
select CompanyName, ContactName, Country, City, Fax
from Suppliers
where Country like 'S%';

-- 14
select CompanyName, ContactName, Country, City, Fax
from Suppliers
where Country like '%a';

-- 15
select CompanyName, ContactName, Country, City, Fax
from Suppliers
where Country like '%an%';

-- 16
select CompanyName, ContactName, Country, City, Fax
from Suppliers
where Country like '__an__';

-- 17
select CompanyName, Country, City
from Customers
where Country like '%land';

-- 18
select TitleOfCourtesy, FirstName, LastName, BirthDate
from Employees;

-- 19
select 
	TitleOfCourtesy || ' ' || FirstName || ' ' || LastName as Emp,
	BirthDate
from Employees;

-- 20
select 
	TitleOfCourtesy || ' ' || FirstName || ' ' || LastName as Emp,
	BirthDate
from Employees
order by BirthDate desc;

-- 21
select 
	TitleOfCourtesy || ' ' || FirstName || ' ' || LastName as Emp,
	BirthDate
from Employees
where BirthDate like '1995%'
order by BirthDate asc;

-- 22
select 
	TitleOfCourtesy || ' ' || FirstName || ' ' || LastName as Emp,
	BirthDate
from Employees
where BirthDate like '____-01%'
order by BirthDate asc;

-- 23
select p.ProductName, s.CompanyName as SupplierCompanyName
from Products p 
join Suppliers s 
on p.SupplierId = s.SupplierId;

-- 24
select p.ProductName, s.CompanyName as SupplierCompanyName, c.CategoryName
from Products p 
join Suppliers s on p.SupplierId = s.SupplierId
join Categories c on p.CategoryId = c.CategoryId;

-- 25
select
	o.OrderId, o.OrderDate, c.CompanyName, 
	e.TitleOfCourtesy || ' ' || e.FirstName || ' ' || e.LastName as Employee,
	s.CompanyName as Shipper
from
	Orders o join
	Customers c on o.CustomerId = c.CustomerId,
	Employees e on o.EmployeeId = e.EmployeeId,
	Shippers s on o.ShipVia = s.ShipperID;

select * from orderInfo;	
drop view orderInfo;

	
-- 26
select 
	count(ProductId) NoOfProduct,
	sum(UnitPrice) SumOfUnitprice,
	max(UnitPrice) MaxOfUnitprice,
	min(UnitPrice) MinOfUnitprice,
	avg(UnitPrice) AverageOfUnitprice
from Products;

-- 27
select 
	c.CategoryName,
	count(p.ProductID) as NoOfProduct
from  Categories c join Products p on c.CategoryId = p.CategoryId
group by 1;

-- 28
select 
	c.CategoryName,
	count(p.ProductID) as NoOfProduct
from  Categories c join Products p on c.CategoryId = p.CategoryId
group by 1 order by 2 desc;

-- 29
select 
	c.CategoryName as CategoryName,
	count(p.ProductID) as NoOfProduct
from  Categories c join Products p on c.CategoryId = p.CategoryId
group by CategoryName having NoOfProduct < 10 
order by NoOfProduct desc;

-- 30
INSERT INTO Categories VALUES (9, 'catname1', null);
INSERT INTO Categories VALUES (10, 'catname2', 'desc2');
-- preview
SELECT * from Categories;

-- 31 
UPDATE Categories
SET Description = 'update desc3'
WHERE CategoryId = 10;

-- 32
DELETE FROM Categories
WHERE CategoryId = 10;

-- FINISH!



