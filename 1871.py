flag = True

while flag==True:
	nrs = input().split()

	nr1 = int(nrs[0])
	nr2 = int(nrs[1])

	soma = nr1 + nr2

	if soma != 0:

		soma1 = str(nr1 + nr2).replace('0', '')

		print(soma1)

	else:
		flag = False
