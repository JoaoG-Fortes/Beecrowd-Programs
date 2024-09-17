# -*- coding: utf-8 -*-

stars = 0
A = int(input())
N = int(input())

for x in range(N):
    F = int(input())

    if A * F >= 40000000:
        stars += 1
    else:
        continue

print(stars)
