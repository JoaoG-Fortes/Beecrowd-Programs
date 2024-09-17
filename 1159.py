flag = True

while flag == True:
	x = int(input())
	pares = 0
	cont = 0

	if x == 0:
		flag = False

	else:
		while cont < 5:
			if x % 2 == 0:
				pares += x
				x += 1
				cont += 1
			else:
				x += 1

		print(pares)
