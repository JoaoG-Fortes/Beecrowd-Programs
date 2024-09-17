stf = input().split()

S = int(stf[0])
T = int(stf[1])
F = int(stf[2])

fuso = S + T + F

if fuso >= 24:
	fuso -= 24
	print(fuso)

elif fuso < 0:
	fuso += 24
	print(fuso)

else:
	print(fuso)
