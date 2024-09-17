N = int(input())

for x in range(0, N):
	valores = input().split()

	a = float(valores[0])
	b = float(valores[1])
	c = float(valores[2])

	media = ((a * 2) + (b * 3) + (c * 5)) / (10)

	print(f'{media:.1f}')
