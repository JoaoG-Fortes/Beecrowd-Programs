soma = 0
quant = 0
Z = 0
X = int(input())

while Z <= X:
	Z = int(input())

for x in range(X-1, Z):
	soma += x

	if soma <= Z:
		quant += 1

	elif soma > Z:
		print(quant)
		break

	else:
		pass
