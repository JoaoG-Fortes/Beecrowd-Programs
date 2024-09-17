disponivel = list(map(int, input().split()))
escolhas = list(map(int, input().split()))
c = 0
b = 0
p = 0

if escolhas[0] >= disponivel[0]:
	c = escolhas[0] - disponivel[0]

if escolhas[1] >= disponivel[1]:
	b = escolhas[1] - disponivel[1]

if escolhas[2] >= disponivel[2]:
	p = escolhas[2] - disponivel[2]

print(c + b + p)
