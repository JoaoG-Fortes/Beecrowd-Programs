# falta terminar!

flag = True
lista = []

while flag == True:
	a = input()
	b = input()

	if len(a) >= 3:

		a = list(a)

		for x in a:
			lista = x
			x = list(x)
			x.append(''.join(a[0, 1, 2]))

		print(x)
