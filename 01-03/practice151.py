def above_avg(t, av):
    return [i for i in t if i > av]
def below_avg(t, av):
    return [i for i in t if i < av]

def check_number(*args, data):
    s = data.split("-")
    n = len(args)
    mx = max(args)
    mn = min(args)
    av = sum(args) / n
    ab = len(above_avg(args, av))
    bl = len(below_avg(args, av))
    result = []
    if 'max' in s:
        result.append(mx)
    if 'min' in s:
        result.append(mn)
    if 'av' in s:
        result.append(av)
    if 'ab' in s:
        result.append(ab)
    if 'bl' in s:
        result.append(bl)
    return result

x,y = check_number(17,22,35,55,67,38,98,109,10,5,77,data="max-min")
print("MAXIMUM = {0}\nMINIMUM = {1}".format(x,y))
x,y = check_number(12,99,34,67,21,98,13,data="ab-bl")
print("ABOVE AVERAGE = {0}\nBELOW AVERAGE = {1}".format(x,y))
