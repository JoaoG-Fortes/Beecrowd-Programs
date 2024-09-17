valor = float(input())

if (valor >= 0.00) and (valor <= 2000.00):
	print("Isento")

else:
	valor -= 2000.00
	if (valor >= 0.01) and (valor <= 1000.00):
		imposto = valor * 0.08
		print(f'R$ {imposto:.2f}')

	elif (valor >= 1000.01) and (valor <= 2500.00):
		valor -= 1000.00
		imposto =(valor * 0.18)+(80.00)
		print(f'R$ {imposto:.2f}')

	elif (valor > 2500.00):
		valor -= 2500.00
		imposto = (valor * 0.28)+(80.00)+(270.00)
		print(f'R$ {imposto:.2f}')
