abcd = input().split()

a = int(abcd[0])
b = int(abcd[1])
c = int(abcd[2])
d = int(abcd[3])

if ((b>c) and (d>a)) and ((c+d)>(a+b)) and ((c>0) and (d>0)) and (a%2 == 0):
	print("Valores aceitos")
else:
	print("Valores nao aceitos")