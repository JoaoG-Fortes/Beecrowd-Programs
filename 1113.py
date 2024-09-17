flag = True

while flag == True:
	xy = input().split()

	x = int(xy[0])
	y = int(xy[1])

	if x == y:
		flag = False

	else:
		if x > y:
			print('Decrescente')

		else:
			print('Crescente')
