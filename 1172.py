i = 0

for x in range(0, 10):
	X = int(input())

	if X <= 0:
		NX = 1

		print(f'X[{i}] = {NX}')

	else:
		print(f'X[{i}] = {X}')

	i += 1
