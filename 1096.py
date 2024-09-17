i = 1
j = 7
cont = 0

while i <= 9:
	print(f'I={i} J={j}')
	cont += 1

	j -= 1

	if cont == 3:
		i += 2
		j = 7
		cont = 0
