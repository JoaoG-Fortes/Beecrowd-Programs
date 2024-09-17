flag = True
ctrl = 0

while flag == True:
	try:
		ano = int(input())
		leap = 0
		ordinary = 1

		if ctrl:
			print("")
		ctrl = 1

		if (ano % 4 == 0) and (not (ano % 100 == 0) or (ano % 400 == 0)):
			print("This is leap year.")
			leap = 1
			ordinary = 0

		if (ano % 15 == 0):
			print("This is huluculu festival year.")
			ordinary = 0

		if (ano % 55 == 0) and leap:
			print("This is bulukulu festival year.")

		if ordinary:
			print("This is an ordinary year.")

	except EOFError:
		flag = False
