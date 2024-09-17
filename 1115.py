flag = True

while flag == True:
	xy = input().split()

	x = int(xy[0])
	y = int(xy[1])

	if (x == 0) or (y == 0):
		flag = False

	else:
		if (x > 0) and (y > 0):
			print('primeiro')

		if (x < 0) and (y > 0):
			print('segundo')

		if (x < 0) and (y < 0):
			print('terceiro')

		if (x > 0) and (y < 0):
			print('quarto')
