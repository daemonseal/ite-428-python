# Using splitlines
def read_data(fname):
    f = open(fname, 'r')
    data = f.read().splitlines()
    # print(data)
    for i, s in enumerate(sorted(data, reverse=True)):
        print("{}.) {}".format(i+1, s.upper()))


read_data('text/MarvelComics.txt')
