casos = int(input())

for x in range(casos):
	soma = 0
	potencia = 0
	n = int(input())

	for y in range(n):

		potencia = 2**y
		soma += potencia

	print(soma)
