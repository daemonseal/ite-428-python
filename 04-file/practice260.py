with open("text/ilovesea.txt", 'r', encoding='utf-8') as f:
    data = f.readlines()
    for i, d in enumerate(data):
        print('{}. - {}'.format(i, d))
