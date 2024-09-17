flag = True
cont = 0

while flag == True:
	lis = []
	X = int(input())

	if X == 0:
		flag = False

	for x in range(1, X+1):
		lis.append(x)

	for i in lis:
		if i == lis[-1]:
			print(i)

		else:
			print(i, end=' ')
