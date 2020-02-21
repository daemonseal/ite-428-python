import csv

n = int(input('Enter Number of New Product : '))

# Write to csv
print("Adding some products to .csv file.")
data = []
for i in range(n):
    print("Product number [{}]".format(i+1))
    print("====================================")
    name = input('Enter product name : ')
    price = input('Enter prodcut price : ')
    stock = input('Enter product stock : ')
    print('')
    d = [name, price, stock]
    data.append(d)

with open('products.csv', 'w') as f:
    fw = csv.writer(f,delimiter=",")
    fw.writerows(data)

# Read from csv

print("Reading from csv. Configuration using .ini file is supported.")

def read_file(fname, splitter):
    # read file and return a list of list that contain strings
    with open(fname, 'r') as f:
        return [row.split(splitter) for row in f.read().splitlines()]


def create_config_dict(config):
    # create a dictionary from the config list
    config_d = {}
    for row in config:
        config_d[row[0]] = row[1]
    return config_d


def calculate_total(d):
    nt = 0
    for r in d:
        total = int(r[1]) + int(r[2])
        r.append(total)
        nt = nt + total
    return d, nt


def format_result(d, nt, config):
    # convert the list of list to suitable format for writing
    # use configuration files to change output style
    if config['comma'] == 'yes':
        config['comma'] = ','
    else:
        config['comma'] = ''
    return '\n'.join([('{:<20} {:>20' + config['comma']
                       + '.'
                       + config['decimal_places'] + 'f}')
                      .format(dp[0], dp[3]) for dp in d]) \
        + '\n{}'.format(config['line'] * 50) \
        + ('\n{:<20} {:>20' + config['comma']
           + '.' + config['decimal_places']
           + 'f} {}').format(
               'Total Value', nt,
               config['currency_unit'])


def read_csv(fname):
    with open(fname, 'r') as f:
        fr = csv.reader(f)
        return list(fr)


# Main program
result, net_total = calculate_total(read_csv('products.csv'))
config_file = create_config_dict(read_file('appConfig.ini', '='))
print(format_result(result, net_total, config_file))
