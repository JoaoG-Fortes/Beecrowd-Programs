flag = True
cont = 0
lis = []

while flag == True:
	nota = float(input())

	if (nota >= 0) and (nota <= 10):
		lis.append(nota)
		cont += 1

		if cont == 2:
			n1 = lis[0]
			n2 = lis[1]
			media = (n1 + n2) / 2
			print(f'media = {media:.2f}')
			flag = False

	else:
		print('nota invalida')
