N = int(input())
N2 = N
flag = True

while flag == True:
	if N2 > 1:
		N = N * (N2-1)
		N2 -= 1
	else:
		print(N)
		break
