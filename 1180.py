cont = 0
N = int(input())
lis = list(map(int, input().split()))
menor = lis[0]

for x in lis[::]:
	if x < menor:
		menor = lis[cont]
		posic = cont
	cont += 1

print(f'Menor valor: {menor}')
print(f'Posicao: {posic}')
