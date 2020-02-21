# Define functions
def calculate(s, a, j):
    return (19.95 * s) + (22.95 * a) + (14.95 * j)
     
# Get input from users
print("Senior : 65 up \nAdult : 18-64 \nJunior : 4-17\nChild : 0-3")
while True:
    try:
        customers = input("Enter number of Senior, Adult, Junior, Child :")
        senior, adult, junior, child = [int(c.strip()) for c in customers.split(",")]
    except:
        print("Please enter valid values eg. 1,2,3,4")
        continue
    else:
        break

total = calculate(senior, adult, junior)

print("Total of Ticket = ${0:.2f}".format(total))