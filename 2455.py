P1, C1, P2, C2 = list(map(int, input().split()))

L = P1*C1
R = P2*C2

if L == R:
	print("0")
elif L > R:
	print("-1")
elif L < R:
	print("1")
