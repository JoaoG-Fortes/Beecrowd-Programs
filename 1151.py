N = int(input())
lis = [0, 1]
i1 = 0
i2 = 1

for x in range(0, N-2):
	lis.append(lis[i1]+lis[i2])
	i1 += 1
	i2 += 1


for i in lis:
		if i == lis[-1]:
			print(i)

		else:
			print(i, end=' ')
