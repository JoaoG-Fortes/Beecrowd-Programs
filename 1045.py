numeros = input().split()
lis = []

for i in range(len(numeros)):
    numeros[i] = float(numeros[i])

numeros.sort(reverse=True)

A = numeros[0]
B = numeros[1]
C = numeros[2]

if (A >= B+C):
	print('NAO FORMA TRIANGULO')

elif A**2 == B**2 + C**2:
	print('TRIANGULO RETANGULO')

elif A**2 > B**2 + C**2:
	print('TRIANGULO OBTUSANGULO')
	if ((A == B) and (B != C) and (C != A)) or ((A != B) and (B == C) and (C != A)) or ((A != B) and (B != C) and (C == A)):
		print('TRIANGULO ISOSCELES')

elif A**2 < B**2 + C**2:
	print('TRIANGULO ACUTANGULO')
	if (A == B) and (B == C) and (C == A):
		print('TRIANGULO EQUILATERO')
	elif ((A == B) and (B != C) and (C != A)) or ((A != B) and (B == C) and (C != A)) or ((A != B) and (B != C) and (C == A)):
		print('TRIANGULO ISOSCELES')
