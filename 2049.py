# falta terminar!

flag = True
instancia = 0

while flag == True:
	assin = int(input())

	if assin != 0:
		instancia += 1
		seq = input()

		assin = str(assin)

		if assin in seq:
			print("Instancia {}".format(instancia))
			print("verdadeira")
			print("")
		else:
			print("Instancia {}".format(instancia))
			print("falsa")
			print("")

	else:
		flag = False
