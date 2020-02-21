def line(t,n):
        print(t*n)

t = "*"
n = 60

line(t,n)
print("{:>32}".format("MENU"))
line(t,n)
print("C or c Area of Circles")
print("S or s Area of Rectangle")
line(t,n)
c = input("Enter Your Choice : ")
line(t,n)
if c == "c" or c == "C":
        r = float(input("Please Input Radius : "))
        area = 3.14*r**2
elif c == "s" or c == "S":
        w = float(input("Please Input Width : "))
        h = float(input("Please Input Lenght : "))
        area = w * h
line(t,n)
print("AREA = {:.2f}".format(area))
