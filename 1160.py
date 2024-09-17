T = int(input())

for x in range(0, T):
	ano = 0
	a = input().split()

	PA = int(a[0])
	PB = int(a[1])
	G1 = float(a[2])
	G2 = float(a[3])

	while PA <= PB:
		PA = int(PA*(1 + G1/100))
		PB = int(PB*(1 + G2/100))
		ano += 1

		if ano > 100:
			print('Mais de 1 seculo.')
			break
	else:
		print(f'{ano} anos.')
