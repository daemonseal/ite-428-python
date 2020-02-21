n = int(input('Enter Number of New Product : '))

data = []
for i in range(n):
    print("Product number [{}]".format(i+1))
    print("====================================")
    name = input('Enter product name : ')
    price = input('Enter prodcut price : ')
    stock = input('Enter product stock : ')
    print('')
    d = '{},{},{}'.format(name, price, stock)
    data.append(d)

with open('text/product.csv', 'w') as f:
    f.write('\n'.join(data))
