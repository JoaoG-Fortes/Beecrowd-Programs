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

			while True:

				print('novo calculo (1-sim 2-nao)')
				x = int(input())
				if x == 1:
					cont = 0
					lis = []
					break

				elif x == 2:
					flag = False
					break

				else:
					pass


	else:
		print('nota invalida')
