T = int(input())

for x in range(T):
	N = int(input())
	lis = [0, 1]
	i1 = 0
	i2 = 1

	for y in range(0, N-1):
		lis.append(lis[i1]+lis[i2])
		i1 += 1
		i2 += 1

	X = lis[N]

	print(f'Fib({N}) = {X}')
