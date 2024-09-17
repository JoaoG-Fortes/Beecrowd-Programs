val = input().split()

horas = int(val[2]) - int(val[0])
minutos = int(val[3]) - int(val[1])

if (horas > 0) and (minutos > 0):
	print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))

elif (horas < 0) and (minutos < 0):
	horas += 23
	minutos += 60
	print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))

elif (horas == 0) and (minutos == 0):
	horas += 24
	print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))

elif (horas > 0) and (minutos < 0):
	if horas < 2:
		horas = 0
		minutos += 60
		print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
	else:
		horas -= 1
		minutos += 60
		print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))

elif (horas < 0) and (minutos > 0):
	horas += 24
	print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))

elif (horas == 0) and (minutos > 0):
	print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))

elif (horas == 0) and (minutos < 0):
	horas += 23
	minutos += 60
	print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))

elif (horas < 0) and (minutos == 0):
	horas += 24
	print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))

elif (horas > 0) and (minutos == 0):
	print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
