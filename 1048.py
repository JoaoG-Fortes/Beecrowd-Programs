sal = float(input())

if (sal >= 0.0) and (sal <= 400.0):
	sal2 = sal + (sal * 0.15)
	reajuste = sal2 - sal
	print(f'Novo salario: {sal2:.2f}')
	print(f'Reajuste ganho: {reajuste:.2f}')
	print(f'Em percentual: 15 %')

elif (sal >= 400.01) and (sal <= 800.00):
	sal2 = sal + (sal * 0.12)
	reajuste = sal2 - sal
	print(f'Novo salario: {sal2:.2f}')
	print(f'Reajuste ganho: {reajuste:.2f}')
	print(f'Em percentual: 12 %')

elif (sal >= 800.01) and (sal <= 1200.00):
	sal2 = sal + (sal * 0.1)
	reajuste = sal2 - sal
	print(f'Novo salario: {sal2:.2f}')
	print(f'Reajuste ganho: {reajuste:.2f}')
	print(f'Em percentual: 10 %')

elif (sal >= 1200.01) and (sal <= 2000.00):
	sal2 = sal + (sal * 0.07)
	reajuste = sal2 - sal
	print(f'Novo salario: {sal2:.2f}')
	print(f'Reajuste ganho: {reajuste:.2f}')
	print(f'Em percentual: 7 %')

elif (sal >= 2000.01):
	sal2 = sal + (sal * 0.04)
	reajuste = sal2 - sal
	print(f'Novo salario: {sal2:.2f}')
	print(f'Reajuste ganho: {reajuste:.2f}')
	print(f'Em percentual: 4 %')
