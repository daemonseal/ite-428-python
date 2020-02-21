Age = int(input("Enter your age: "))
if Age > 18:
    print("Can vote")
elif Age > 60:
    print("Too old")
else:
    print("Cant vote")