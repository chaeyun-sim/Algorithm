for _ in range(3):
    yut = [int(i) for i in input().split()]

    if sum(yut) == 1: print('C')
    elif sum(yut) == 2: print('B')
    elif sum(yut) == 3: print('A')
    elif sum(yut) == 4: print('E')
    else: print('D')