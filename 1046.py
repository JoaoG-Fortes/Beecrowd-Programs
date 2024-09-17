val = input().split()

duracao = int(val[1]) - int(val[0])

if duracao > 0:
	print('O JOGO DUROU {} HORA(S)'.format(duracao))
else:
	duracao = duracao + 24
	print('O JOGO DUROU {} HORA(S)'.format(duracao))
