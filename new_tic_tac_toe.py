def postr(a, b, zn):
    pole = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

    pole[a][b] = zn

    for i in pole:

        for i1 in i:
            print(i1, end=' ')

        print()

    return pole