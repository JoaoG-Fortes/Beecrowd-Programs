# -*- coding: utf-8 -*-

while True:
    fatorial1 = 1
    fatorial2 = 1

    try:
        M, N = list(map(int, input().split()))
        c = 1

        if M == 0 and N == 0:  # SE OS DOIS NÚMEROS FOREM '0'
            fatorial1, fatorial2 = 1, 1

        elif M == 0 and N != 0:  # SE O PRIMEIRO NÚMEOR FOR '0' E O SEGUNDO NÃO
            fatorial1 = 1

            c = 1
            for x in range(N):
                fatorial2 = fatorial2 * c
                c += 1

        elif M != 0 and N == 0:  # SE O SEGUNDO NÚEMRO FOR '0' E O SEGUNDO NÃO
            fatorial2 = 1

            c = 1
            for x in range(M):
                fatorial1 = fatorial1 * c
                c += 1

        else:  # SE NENHUM DOS NÚMEROS É '0'
            c = 1
            for x in range(M):
                fatorial1 = fatorial1 * c
                c += 1

            c = 1
            for x in range(N):
                fatorial2 = fatorial2 * c
                c += 1

        soma = fatorial1 + fatorial2
        print(soma)

    except EOFError:
        break
