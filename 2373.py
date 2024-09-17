N = int(input())
quebrou = 0

for x in range(N):
	L, C = list(map(int, input().split()))

	if L > C:
		quebrou += C

print(quebrou)
