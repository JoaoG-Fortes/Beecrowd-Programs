N = int(input())

total = 0
c = 0
r = 0
s = 0

for x in range(0, N):
	cobaia = input().split()

	quantia = int(cobaia[0])
	tipo = cobaia[1]

	if tipo == 'C':
		c += quantia

	elif tipo == 'R':
		r += quantia

	elif tipo == 'S':
		s += quantia

	total += quantia


per_c = (c * 100) / total
per_r = (r * 100) / total
per_s = (s * 100) / total

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {c}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')
print(f'Percentual de coelhos: {per_c:.2f} %')
print(f'Percentual de ratos: {per_r:.2f} %')
print(f'Percentual de sapos: {per_s:.2f} %')
