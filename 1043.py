abc = input().split()
lis = []

for x in abc:
	lis.append(float(x))

A = lis[0]
B = lis[1]
C = lis[2]

if (A + B > C) and (B + C > A) and (C + A > B):
	per = A + B + C
	print(f'Perimetro = {per}')

else:
	area = (((A + B) * C) / 2)
	print(f'Area = {area}')
