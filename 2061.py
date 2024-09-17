# -*- coding: utf-8 -*-

N, M = list(map(int, input().split()))

for i in range(M):

    acao = input()

    if acao == "fechou":
        N += 1

    elif acao == "clicou":
        N -= 1

print(N)
