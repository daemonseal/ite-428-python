def read_file(fname, splitter):
    # read file and return a list of list that contain strings
    with open(fname, 'r') as f:
        return [row.split(splitter) for row in f.read().splitlines()]


def calculate_total(data):
    # calculate and append total value to the list
    # return [d.append(float(d[1])*float(d[2])) for d in data]
    net_total = 0
    for d in data:
        total = float(d[1]) * float(d[2])
        d.append(total)
        net_total += total
    return data, net_total


def create_config_dict(config):
    # create a dictionary from the config list
    config_d = {}
    for row in config:
        config_d[row[0]] = row[1]
    return config_d


def format_result(data, net_total, config):
    # convert the list of list to suitable format for writing
    # use configuration files to change output style
    if config['comma'] == 'yes':
        config['comma'] = ','
    else:
        config['comma'] = ''
    return '\n'.join([('{:<20} {:>20' + config['comma']
                       + '.'
                       + config['decimal_places'] + 'f}')
                      .format(d[0], d[3]) for d in data]) \
        + '\n{}'.format(config['line'] * 50) \
        + ('\n{:<20} {:>20' + config['comma']
           + '.' + config['decimal_places']
           + 'f} {}').format(
               'Total Value', net_total,
               config['currency_unit'])


data, net_total = calculate_total(
    read_file('practice267-files/products.csv', ',')
)
config = create_config_dict(read_file('practice267-files/appConfig.ini', '='))
result = format_result(data, net_total, config)
print(result)
