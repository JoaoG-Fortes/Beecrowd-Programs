var1 = input()
var2 = input()
var3 = input()

if var1 == 'vertebrado':
	if var2 == 'ave':
		if var3 == 'carnivoro':
			print('aguia')
		elif var3 == 'onivoro':
			print('pomba')

	elif var2 == 'mamifero':
		if var3 == 'onivoro':
			print('homem')
		elif var3 == 'herbivoro':
			print('vaca')


elif var1 == 'invertebrado':
	if var2 == 'inseto':
		if var3 == 'hematofago':
			print('pulga')
		elif var3 == 'herbivoro':
			print('lagarta')

	elif var2 == 'anelideo':
		if var3 == 'hematofago':
			print('sanguessuga')
		elif var3 == 'onivoro':
			print('minhoca')
