flag = True

while flag == True:
	soma = 0
	mn = input().split()

	m = int(mn[0])
	n = int(mn[1])

	if (m <= 0) or (n <= 0):
		flag = False

	else:
		if m >= n:
			for i in range(n, m+1):
				soma += i
				print(f'{i} ', end='')
			print(f'Sum={soma}')

		else:
			for i in range(m, n+1):
				soma += i
				print(f'{i} ', end='')
			print(f'Sum={soma}')
