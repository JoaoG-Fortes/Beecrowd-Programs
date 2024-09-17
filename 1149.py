lis = list(map(int, input().split()))
a = int(lis[0])
n = 0
soma = 0

for x in lis[1::1]:
	if x <= 0:
		pass
	else:
		n = int(x)

for x in range(n):
	soma += a
	a += 1

print(soma)
