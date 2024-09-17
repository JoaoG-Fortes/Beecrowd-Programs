anos = 0
meses = 0
dias = int(input())


if dias < 30:
	dias = dias
	meses = 0
	anos = 0


elif dias == 30:
	dias = 0
	meses += 1


elif (dias > 30) and (dias < 365):

	while dias >= 30:
		dias -= 30
		meses += 1


elif dias > 365:

	while dias > 365:
		dias = dias-365
		anos += 1

	while dias > 30:
		dias = dias-30
		meses += 1


print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))