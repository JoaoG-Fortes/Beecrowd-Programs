flag = True
alc = 0
gas = 0
die = 0

while flag == True:
	tipo = int(input())

	if tipo == 1:
		alc += 1

	elif tipo == 2:
		gas += 1

	elif tipo == 3:
		die += 1

	elif tipo == 4:
		flag = False

	else:
		pass

print('MUITO OBRIGADO')
print(f'Alcool: {alc}')
print(f'Gasolina: {gas}')
print(f'Diesel: {die}')
