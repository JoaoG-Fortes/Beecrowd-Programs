flag = True
grenais = 0
vint = 0
vgre = 0
empa = 0

while flag == True:
	grenais += 1
	xy = input().split()

	x  = int(xy[0])
	y  = int(xy[1])

	if x > y:
		vint += 1
	elif x < y:
		vgre += 1
	else:
		empa += 1

	print('Novo grenal (1-sim 2-nao)')
	opcao = int(input())

	if opcao == 1:
		pass
	else:
		flag = False

print(f'{grenais} grenais')
print(f'Inter:{vint}')
print(f'Gremio:{vgre}')
print(f'Empates:{empa}')

if vint > vgre:
	print('Inter venceu mais')
else:
	print('Gremio venceu mais')
