a = 1
b = 2
c = 1+(a/b)
for x in range(2,100):
	b += 1
	d = c + (a/b)
	c = d
print("{:.2f}".format(c)),
