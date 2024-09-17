flag = True
i = 1
j = 7

while flag==True:
	jf = j
	for x in range(0, 3):
		print("I={} J={}".format(i, jf))
		jf -= 1
	i += 2
	j += 2

	if j == 17:
		flag = False