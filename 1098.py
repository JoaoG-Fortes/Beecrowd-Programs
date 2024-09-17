i = 0
j = 1
cont = 0

while i <= 2:
	cont += 1
	if i == 0:
		for x in range(0, 3):
			print(f'I={i} J={j}')
			j += 1
	
	if cont == 6:
		for x in range(0, 3):
			print(f'I={i:.0f} J={j:.0f}')
			j += 1
			cont = 1

	elif i != 0:
		for x in range(0, 3):
			print(f'I={i:.1f} J={j:.1f}')
			j += 1

	i += 0.2
	j -= 3
	j += 0.2
