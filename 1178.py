N = float(input())
i = 0

for x in range(100):
	print(f'N[{i}] = {N:.4f}')
	N /= 2
	i += 1
