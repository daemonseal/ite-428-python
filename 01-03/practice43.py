# From slide 43

def line(t,n):{
        print(t*n)
}

price = float(input("Enter Price of Product           :"))
amount = int(input("Enter Amount of Product          :"))
total = price * amount
vat = total * 0.07

line("*",55)
line("-",55)
print("PRICE             : {0:30,.2f} Baht".format(price))
print("AMOUNT            : {0:30,}".format(amount))
print("SUBTOTAL          : {0:30,.2f}".format(total))
line("-",55)
print("VAT (7%)          : {0:30,.2f} Baht".format(vat))
print("GRAND TOTAL       : {0:30,.2f} Baht".format(total + vat))
line("-",55)
line("*",55)
