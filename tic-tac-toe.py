def board(column):
    print(('___') * column + '_')
    for _ in range(column):
        print('|__' * column + '|')


board(3)