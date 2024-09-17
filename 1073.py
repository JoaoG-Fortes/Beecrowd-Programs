N = int(input())

if N % 2 == 0:
	for x in range(2, N+1, 2):
		print(f'{x}^2 =', x**2)

else:
	N += 1
	for x in range(2, N, 2):
		print(f'{x}^2 =', x**2)
