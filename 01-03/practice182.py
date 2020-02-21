# This solution does not require external set of prime numbers

def Types_of_integer(*int_tuple):
    for i in sorted(list(set(int_tuple))):
        print(find_number(i))
    print('')

def find_number(i):
    for d in range(2, i):
        if i % d == 0:
            return '{} : Composite Number'.format(i)
    return '{} : Prime Number'.format(i)

if __name__ == '__main__':
    Types_of_integer(10,9,22,32,45,9,2,103,71,45)
    Types_of_integer(49,37,14,37)
