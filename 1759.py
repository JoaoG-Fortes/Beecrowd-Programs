num = int(input())
cont = 0

for x in range(0, num):
	print("Ho", end='')
	cont += 1

	if cont < num:
		print(" ", end='')
	elif cont == num:
		break

print("!")
