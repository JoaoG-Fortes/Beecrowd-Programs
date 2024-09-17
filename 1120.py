sal = 0
nrerro = 0
uaieutru = True

while uaieutru == True:
	valores = input().split()
	nrerro = valores.pop(0)
	sal = valores[0]

	if (nrerro != '0') and (sal != '0'):
		sal = list(sal)
		for x in sal[0::1]:
			if x == nrerro:
				sal.remove(x)
			else:
				pass

		try:
			print(int(''.join(sal)))
		except:
			print(0)

	else:
		uaieutru = False
