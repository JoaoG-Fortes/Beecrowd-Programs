# -*- coding: utf-8 -*-


while True:
    try:
        n1, n2 = list(map(int, input().split()))
        diferenca = n2 - n1
        if diferenca >= 0:
            print(diferenca)
        else:
            print(diferenca*-1)

    except:
        EOFError
        break
