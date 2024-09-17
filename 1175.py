lis = []

for x in range(20):
	Y = int(input())

	lis.append(Y)

dec = 19

for i in range(0, 10):
	lis[i], lis[dec] = lis[dec], lis[i]
	dec -= 1

for j in lis[::1]:
	print(f'N[{lis.index(j)}] = {j}')
