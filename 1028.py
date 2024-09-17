casos = int(input())

for x in range(casos):

	f1, f2 = list(map(int, input().split()))

	while (f2 != 0):
		r = f1 % f2
		f1 = f2
		f2 = r

	print(f1)
