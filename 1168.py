dic = {"1" : 2, "2" : 5, "3": 5, "4" : 4, "5" : 5, "6" : 6, "7" : 3, "8" : 7, "9" : 6, "0" : 6}
num = int(input(""))
for x in range(num):
	tst = str(input(""))
	lista = []
	leds = 0

	for z in tst:
		lista.append(z)

	for y in lista:
		leds = leds+dic[y]

	print (leds,"leds")
