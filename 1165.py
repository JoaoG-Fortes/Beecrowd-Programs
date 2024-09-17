N = int(input())

for x in range(0, N):
	div = 0
	X = int(input())

	for i in range(1, X):
		if X % i == 0:
			div += i
		else:
			pass

	if div > 2:
		print(f'{X} nao eh primo')
	else:
		print(f'{X} eh primo')
