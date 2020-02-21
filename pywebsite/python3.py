#!\xampp\htdocs\mywebsite\venv\Scripts\python
import cgi

form = cgi.FieldStorage()
c = int(form.getvalue("col"))
r = int(form.getvalue("row"))
t = form.getvalue("text")

from random import randint


def rand_pic():
    return str(randint(0, 5))


def a(obj):
    return "<a href='#'>" + obj + "</a>"


print("Context-type:text/html\n")
print("<html>")
print("<head><title>My First Web</title></head>")
print("<body>")
# ---------table-start---------
print("<table style='border: solid 1px black'>")

for i in range(r):
    # ---------tr-start---------
    print("<tr>")
    for j in range(c):
        # ---------td-start---------
        print("<td style='border: solid 1px black; ")
        print("background-color: ")
        if i % 2 == 0:
            print("powderblue")
        else:
            print("lightpink")
        print(";'>")
        # ---------img-or-text---------
        if i == 0 or j == 0 or i == r - 1 or j == c - 1:
            output = "<img src='img/{}.jpeg' height='50' width='50'>".format(rand_pic())
        else:
            output = t
        if i == j:
            output = a(output)
        print(output)
        # ---------td-end---------
        print("</td>")
    # ---------tr-end---------
    print("</tr>")
# ---------table-end---------
print("</table>")
print("</body>")
print("</html>")
