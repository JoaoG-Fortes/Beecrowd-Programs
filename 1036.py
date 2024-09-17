x1 = 0.0
x2 = 0.0
abc = input().split()

a = float(abc[0])
b = float(abc[1])
c = float(abc[2])

delta = ((b**2)-(4*a*c))

if delta <= 0 or a == 0:
	print("Impossivel calcular")

elif delta > 0:
	x1 = ((-b)+delta**(1/2))/(2*a)
	x2 = ((-b)-delta**(1/2))/(2*a)
	print("R1 = {:.5f}\nR2 = {:.5f}".format(x1,x2))