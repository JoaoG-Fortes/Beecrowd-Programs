n = int(input())

for x in range(0, n):
	cont = 0
	impares = 0
	x, y = list(map(int, input().split()))

	while cont < y:
		if x % 2 != 0:
			impares += x
			x += 1
			cont += 1
		else:
			x += 1

	print(impares)
