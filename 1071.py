a = int(input())
b = int(input())

impar = 0

if a >= b:
	for x in range(b+1, a):
		if x % 2 != 0:
			impar += x
else:
	for x in range(a+1, b):
		if x % 2 != 0:
			impar += x

print(impar)
