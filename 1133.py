n1 = int(input())
n2 = int(input())

if n1 > n2:
	for x in range(n2+1, n1):
		if (x % 5 == 2) or (x % 5 == 3):
			print(x)

if n1 < n2:
	for x in range(n1+1, n2):
		if (x % 5 == 2) or (x % 5 == 3):
			print(x)
