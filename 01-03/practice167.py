def line():
    print("-"*30)

flowelrs = ["Sun flower","Ivy","Jusmine","Lily"]
print("Find item in list ignoring case (Type :q to exit)")
while True:
    search = input("Enter flower that you want to search : ")
    if search == ':q':
        break
    print(search.lower() in map(lambda x: x.lower(), flowers))
