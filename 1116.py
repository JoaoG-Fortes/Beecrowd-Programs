N = int(input())

for x in range(0, N):
	xy = input().split()

	x = int(xy[0])
	y = int(xy[1])

	if y == 0:
		print('divisao impossivel')

	else:
		divisao = x / y
		print(f'{divisao:.1f}')
