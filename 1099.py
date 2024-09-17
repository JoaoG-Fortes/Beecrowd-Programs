N = int(input())
impar = 0

for x in range(0, N):
	impar = 0
	xy = input().split()

	X = int(xy[0])
	Y = int(xy[1])

	if X >= Y:
		for i in range(Y+1, X):
			if i % 2 != 0:
				impar += i

	else:
		for i in range(X+1, Y):
			if i % 2 != 0:
				impar += i

	print(impar)
