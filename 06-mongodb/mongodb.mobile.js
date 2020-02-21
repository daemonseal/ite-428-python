show dbs;
use MobileShop;
db.createCollection("Products");
db.Products.insert({"pid":"p001","pname":"Liquid Zest 4G","pbrand":"Acer","pprice":12000,"psize":5});
db.Products.insert({"pid":"p002","pname":"A83 (2018)","pbrand":"OPPO","pprice":7800,"psize":5.7});
db.Products.insert({"pid":"p003","pname":"Motion","pbrand":"BlackBerry","pprice":9000,"psize":4.5});
db.Products.insert({"pid":"p004","pname":"V11i","pbrand":"Vivo","pprice":8990,"psize":6.3});
db.Products.insert({"pid":"p005","pname":"X20 Plus UD","pbrand":"Vivo","pprice":12000,"psize":6.11});
db.Products.insert({"pid":"p006","pname":"G6 Plus","pbrand":"Moto","pprice":5890,"psize":5.9});
db.Products.insert({"pid":"p007","pname":"K8 (2018)","pbrand":"LG","pprice":20200,"psize":5});
db.Products.insert({"pid":"p008","pname":"X4+","pbrand":"LG","pprice":3000,"psize":4.5});
db.Products.insert({"pid":"p009","pname":"X500","pbrand":"LG","pprice":2500,"psize":5.5});
db.Products.insert({"pid":"p010","pname":"Pixel 3 XL","pbrand":"Google","pprice":30000,"psize":6.7});
db.Products.insert({"pid":"p011","pname":"Sunny2 Plus","pbrand":"Wiko","pprice":2350,"psize":5});
db.Products.insert({"pid":"p012","pname":"Galaxy A8s","pbrand":"Samsung","pprice":20030,"psize":6.4});
db.Products.insert({"pid":"p013","pname":"Galaxy J4 Core","pbrand":"Samsung","pprice":9999,"psize":5.4});
db.Products.insert({"pid":"p014","pname":"V6","pbrand":"Haixu","pprice":4890,"psize":6.1});
db.Products.insert({"pid":"p015","pname":"Galaxy Note 9","pbrand":"Samsung","pprice":30000,"psize":6.4});
db.Products.insert({"pid":"p016","pname":"iPhone XS Max","pbrand":"Apple","pprice":43900,"psize":6.5});
db.Products.insert({"pid":"p017","pname":"Iconia Talk S","pbrand":"Acer","pprice":7000,"psize":7});
db.Products.insert({"pid":"p018","pname":"A73","pbrand":"OPPO","pprice":2500,"psize":3.5});
db.Products.insert({"pid":"p019","pname":"Xperia XZ3","pbrand":"Sony","pprice":25000,"psize":6});
db.Products.insert({"pid":"p020","pname":"Xperia XA2","pbrand":"Sony","pprice":4500,"psize":5.2});
db.Products.insert({"pid":"p021","pname":"Xperia XZ2 Premium","pbrand":"Sony","pprice":38900,"psize":5.2});
db.Products.insert({"pid":"p022","pname":"Desire 12s","pbrand":"HTC","pprice":12000,"psize":5.7});
db.Products.insert({"pid":"p023","pname":"U12 life","pbrand":"HTC","pprice":40000,"psize":6});
db.Products.insert({"pid":"p024","pname":"U11 Eyes","pbrand":"HTC","pprice":10000,"psize":7.2});
db.Products.insert({"pid":"p025","pname":"View2 Go","pbrand":"Wiko","pprice":20000,"psize":5.93});
db.Products.insert({"pid":"p026","pname":"Mi Play","pbrand":"Xiaomi","pprice":8990,"psize":5.84});
db.Products.insert({"pid":"p027","pname":"TOMMY3 PLUS","pbrand":"Wiko","pprice":2000,"psize":5.45});
db.Products.insert({"pid":"p028","pname":"8.1","pbrand":"Nokia","pprice":16500,"psize":6.18});
db.Products.insert({"pid":"p029","pname":"Mi Mix 3","pbrand":"Xiaomi","pprice":11111,"psize":6.39});
db.Products.insert({"pid":"p030","pname":"Pixel 3","pbrand":"Google","pprice":10500,"psize":6.5});
db.Products.insert({"pid":"p031","pname":"Zenfone Max (M2) ZB633KL","pbrand":"Asus","pprice":15000,"psize":6.3});
db.Products.insert({"pid":"p032","pname":"Mate 20 X","pbrand":"Huawei","pprice":18000,"psize":7.2});
db.Products.insert({"pid":"p033","pname":"S5 Pro GT","pbrand":"Lenovo","pprice":10000,"psize":6.2});
db.Products.insert({"pid":"p034","pname":"iPhone XS","pbrand":"Apple","pprice":39900,"psize":5.8});
db.Products.insert({"pid":"p035","pname":"Honor 7C","pbrand":"Huawei","pprice":8000,"psize":5.99});
db.Products.insert({"pid":"p036","pname":"A7","pbrand":"OPPO","pprice":12000,"psize":6.2});
db.Products.insert({"pid":"p037","pname":"Galaxy A8s","pbrand":"Samsung","pprice":23456,"psize":6.4});
db.Products.insert({"pid":"p038","pname":"Nova 4","pbrand":"Huawei","pprice":20000,"psize":6.4});
db.Products.insert({"pid":"p039","pname":"K5 Note (2018)","pbrand":"Lenovo","pprice":17500,"psize":6});
db.Products.insert({"pid":"p040","pname":"Zenfone 5z","pbrand":"Asus","pprice":2500,"psize":6.2});
db.Products.insert({"pid":"p041","pname":"Red Magic Mars","pbrand":"Nubia","pprice":25000,"psize":{"x":3.5,"y":5}});

// Select stuff
db.Products.find({});
// First parameter is condition, Second parameter contains fields
db.Products.find({}, {'pname': 1, 'pprice': 1}); // Select only pname and pprice, if not specified, select *
db.Products.find({}, {'pname': 1, 'pprice': 1}).limit(5); // Limiting results to 5
db.Products.find({}).sort({'pprice': 1}); // Sorting 1 - ASC, -1 - DESC
db.Products.find({}).sort({'pprice': 1, 'pbrand': 1}); // Using two sorting keys
db.Products.find({}).sort({'pprice': 1, 'pbrand': 1}).limit(5); // Find, sort, then limit results to 5 
db.Products.find({}).count();
// Select with condition
db.Products.find({'pprice':9000}); // Select from Products where pprice = 9000
db.Products.find({'pprice':{'$gt':10000}}); // Select from Products where pprice > 10000
db.Products.find({'psize':{'$lt':6.0}}); // Select from Products where psize < 6.0
db.Products.find({'pbrand':{'$in':['Apple','Huawei','LG']},'pprice':{'$gt':20200}}); // Select from Products where pbrand in ...
db.Products.find({'psize.x':{'$eq':3.5}}); // Select with hierarchy
db.Products.find({'year':{'$exists':true}}); // Checking if the document exists
db.Products.find({ '$and': [{ 'pprice': { '$gt':10000}}, {'psize': {'$gt':5}}]});
db.Products.find({'$or': [{'pbrand':'LG'}, {'pprice': {'$lt':6000}}]})
// Insert new field
db.Products.insert({'pid':'p042','year': 2562});

