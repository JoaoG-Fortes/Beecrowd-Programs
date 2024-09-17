T = int(input())
v = 0
i = 0

for x in range(1000):
	if v < T:
		print(f'N[{i}] = {v}')
		v += 1
		i += 1
	else:
		v = 0
		print(f'N[{i}] = {v}')
		v += 1
		i += 1
