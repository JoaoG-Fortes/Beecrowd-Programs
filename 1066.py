par = 0
impar = 0
negativo = 0
positivo = 0


for x in range(0, 5):
	a = int(input())

	if a % 2 == 0:
		par += 1

	if a % 2 != 0:
		impar += 1

	if a > 0:
		positivo += 1

	if a < 0:
		negativo += 1


print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')
