# -*- coding: utf-8 -*-

for x in range(int(input())):
    N = int(input())
    if (N > 2) and (N % 2 == 0):
        print('Not Prime')
    elif N == 2:
        print('Prime')
    else:
        y = 3
        while y < N:
            if N % y == 0:
                break
            y += 2
        if y == N:
            print('Prime')
        else:
            print('Not Prime')
