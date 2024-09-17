T = int(input())
abcde = list(map(int, input().split()))
certo = 0

for x in abcde[::]:
	if x == T:
		certo += 1

print(certo)
