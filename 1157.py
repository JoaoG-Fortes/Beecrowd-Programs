N = int(input())
div = 1

for x in range(0, N):
	if N%div == 0:
		print(div)
		div += 1
	else:
		div += 1
