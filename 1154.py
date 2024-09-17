flag = True
t, c = 0, 0

while flag == True:
	a = int(input())

	if a <= 0:
		print(f'{t/c:.2f}')
		flag = False

	else:
		c += 1
		t += a
