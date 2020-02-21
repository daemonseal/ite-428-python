# Define function
def process_name(n):
    return n.lower().split()
def find_email (n):
    return '{}.{}_st@tni.ac.th'.format(n[1][:2],n[0])

# Get input from users
while True:
    try:
        name = input("Please Enter your full name : ")
        print('Your Thai-Nichi student E-mail is "{}"'.format(find_email(process_name(name))))
    except:
        print("Please enter valid values eg. FirstName LastName")
        continue
    else:
        break