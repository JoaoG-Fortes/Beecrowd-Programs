mult = 0
N = int(input())

for x in range(0, N):
	lis = []
	tv = input().split()
	for x in tv:
		lis.append(int(x))

	t = lis[0]
	v = lis[1]

	mult += t * v

print (mult)
