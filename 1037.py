nr = float(input())

if (nr >= 0) and (nr <= 25.00):
	print("Intervalo [0,25]")

elif (nr >= 25.00) and (nr <= 50.00):
	print("Intervalo (25,50]")

elif (nr >= 50.00) and (nr <= 75.00):
	print("Intervalo (50,75]")

elif (nr >= 75.00) and (nr <= 100.00):
	print("Intervalo (75,100]")

else:
	print("Fora de intervalo")