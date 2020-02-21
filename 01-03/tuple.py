#tuple

t1 = ("Boon", 40, "TNI")
t2 = 150.5, 15, 60, "Test"
print(type(t2))
print(t1[0])
print(len(t1))
for x in range(len(t1)):
    print(t1[x])

for x in t1:
    print(x)

for i,m in enumerate(t1):
    print("{} {}".format(i,m))

print(t1 + t2)
t4 = (1, 2, 8, 5, 6, 2, 3)
print(t4) # t4 is a tuple
print(sorted(t4)) # sorted(t4) is a list 
