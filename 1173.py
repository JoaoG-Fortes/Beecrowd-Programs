v = int(input())
i = 0

print(f'N[{i}] = {v}')

for x in range(9):
	i += 1
	v *= 2
	print(f'N[{i}] = {v}')
