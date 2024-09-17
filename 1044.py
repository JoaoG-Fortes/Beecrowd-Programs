lis = []
num = input().split()

for x in num:
	lis.append(int(x))

lis.sort()


num1 = lis[0]
num2 = lis[1]

if num2 % num1 == 0:
	print("Sao Multiplos")

else:
	print("Nao sao Multiplos")
