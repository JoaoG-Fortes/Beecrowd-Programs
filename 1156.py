a = 3
b = 2
c = 1 + (a/b)
for x in range(2,20):
	a += 2
	b = b * 2
	d = c + (a/b)
	c = d
print("{:.2f}".format(c))
