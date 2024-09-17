# -*- coding: utf-8 -*-


# TODO
encaixa = None
N = int(input())

for x in range(1, N):
    A, B = list(map(int, input().split()))

    strA = str(A)
    strB = str(B)

    for i in range(-1, len(strB), -1):
        if strA[i] == strB[i]:
            encaixa = True
        else:
            break

    if encaixa == True:
        print('encaixa')
    else:
        print('nao encaixa')
