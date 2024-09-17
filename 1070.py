a = int(input())

if a % 2 == 0:
	a += 1
	for x in range(0, 6):
		print(a)
		a += 2
elif a % 2 == 1:
	for x in range(0, 6):
		print(a)
		a += 2