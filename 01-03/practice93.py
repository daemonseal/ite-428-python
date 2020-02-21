# Practice 93

def line(t, n):
    """
    This function create a line by printing [t] character for [n] times.
    t:string = a character to print.
    n:int = a number of times to print.
    """
    print(t * n)

# Declare variables for line()
t = "="
n = 50


# Main program starts here
line(t,n)
print("Grade calculator.")
print("This program calculates your grade based your score.")
line(t,n)

# Take input from users
# Valid values are 0 - 100
while True:
    midterm = int(input("Please enter your midterm score (30%): "))
    if 0 <= midterm <= 100:
        break
while True:
    final = int(input("Please enter your final score (50%): "))
    if 0 <= final <= 100:
        break
while True:
    homework = int(input("Please enter your homework score (20%): "))
    if 0 <= homework <= 100:
        break
line(t,n)

# Calculate the total score
total = (midterm * 0.3) + (final * 0.5) + (homework * 0.2)

# Use interval comparison for readabliity
if 97 <= total <= 100:
    grade = "A+"
elif 93 <= total <= 96 :
    grade = "A"
elif 90 <= total <= 92 :
    grade = "A-"
elif 87 <= total <= 89 :
    grade = "B+"
elif 83 <= total <= 86 :
    grade = "B"
elif 80 <= total <= 82 :
    grade = "B-"
elif 77 <= total <= 79 :
    grade = "C+"
elif 73 <= total <= 76 :
    grade = "C"
elif 70 <= total <= 72 :
    grade = "C-"
elif 67 <= total <= 69 :
    grade = "D+"
elif 63 <= total <= 66 :
    grade = "D"
elif 60 <= total <= 62 :
    grade = "D-"
else:
    grade = "F"

# Print results
print("Your total score is: {0:.2f}".format(total))
print("You get {}".format(grade))

# Bonus
if grade == "A+":
    print("Excellent job :)")
elif grade == "F":
    print("Try harder :(")

line(t,n)
# End