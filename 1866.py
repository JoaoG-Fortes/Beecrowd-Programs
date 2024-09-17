C = int(input())

for x in range(0, C):
	cont = 1
	lis = []
	tentativa = int(input())
	for y in range(0, tentativa):
		if cont % 2 == 0:
			lis.append(-1)
		elif cont % 2 == 1:
			lis.append(1)
		cont += 1

	result = sum(lis)
	print(result)
