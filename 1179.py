lispar = []
lisimp = []
cont = 0

for x in range(15):
	N = int(input())


	if N % 2 == 0:
		lispar.append(N)

	else:
		lisimp.append(N)



	if len(lispar) == 5:
		for i in lispar:
			print(f"par[{cont}] = {i}")
			cont += 1

		lispar = []
		cont = 0


	if len(lisimp) == 5:
		for j in lisimp:
			print(f"impar[{cont}] = {j}")
			cont += 1

		lisimp = []
		cont = 0


for j in lisimp:
	print(f"impar[{cont}] = {j}")
	cont += 1

cont = 0

for i in lispar:
	print(f"par[{cont}] = {i}")
	cont += 1
