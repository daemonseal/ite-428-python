import os.path

with open("text/province.txt",'r',encoding='utf-8') as f:
    data = f.read().splitlines()
    for d in data:
        print(d)

with open("text/ilovesea.txt",'r',encoding='utf-8') as f:
    data = f.read().splitlines()
    for d in data:
        print(d)
