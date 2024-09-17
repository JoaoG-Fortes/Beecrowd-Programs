cont = 0
maior = 0
posicao = 0

for x in range(0, 100):
	cont += 1
	a = int(input())
	if a > maior:
		maior = a
		posicao = cont

print(maior)
print(posicao)
