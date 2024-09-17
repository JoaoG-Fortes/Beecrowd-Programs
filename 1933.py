# -*- coding: utf-8 -*-

"""Este códoigo serve para resolver o seguinte problema: existe um jogo
que consiste em montar trios de cartas de um baralho. Os naipes são ignorados
e só a numeração é que conta. Vence quem tiver o trio ou dupla com maior valor,
sendo que o que determina o valor de cada carta é a sua numeração. O código recebe
dois valores, referentes a duas cartas qua já estão na mão do jogador e determinda
qual seria a terceira carta que maximizaria a chance de ele vencer o jogo."""


naipe_1, naipe_2 = list(map(int, input().split()))

if naipe_1 == naipe_2:
    print(naipe_2)

elif naipe_1 > naipe_2:
    print(naipe_1)

elif naipe_1 < naipe_2:
    print(naipe_2)
