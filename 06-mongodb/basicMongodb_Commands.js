// Javascript *js
show dbs;
use tnidatabase;
db.createCollection("students");
db.createCollection("teachers");

// insert data to collection
db.students.insert({'id':'601212451-8','name':'Adisak'});
db.students.insert({'id':'601212451-9','name':'Salinla','age':48});
db.students.find({});