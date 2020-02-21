import math

def str_to_tuple(s):
    s = s.strip().split()
    if len(s) != 2:
        raise ValueError("Please input valid value, such as 2 4")
    return tuple([float(p) for p in s])

def cal_area(p1, p2, p3):
    x1, x2, x3 = p1[0] , p2[0] , p3[0]
    y1, y2, y3 = p1[1] , p2[1] , p3[1]
    return abs((x1*(y2-y3)) - (x2*(y1-y3)) + (x3*(y1-y2)))*0.5

p1 = str_to_tuple(input("Point 1 : "))
p2 = str_to_tuple(input("Point 2 : "))
p3 = str_to_tuple(input("Point 3 : "))
print("Area is : {}".format(cal_area(p1, p2, p3)))
