N = int(input())
N2 = N * 2
a = 0
cont = 0

for x in range(0, N2):
	if (cont % 2 == 0):
		a += 1
		b = a * a
		c = a * b
		print(a, b, c)
		cont += 1
	else:
		b = a * a
		c = a * b
		b += 1
		c += 1
		print(a, b, c)
		cont += 1
