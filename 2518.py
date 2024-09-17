# falta terminar!

from math import sqrt

while True:
	try:
		T = int(input())
		a = input().split()

		h = int(a[0])/100
		c = int(a[1])/100
		l = int(a[2])/100

		hip = sqrt(((h)**2)+((c)**2))

		A = (hip*(l))*T

		print("{:.4f}".format(A))

	except:
		EOFError