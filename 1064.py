med = 0
contante = 0
positivos = 0
for x in range(0,6):
	nr = float(input())

	if nr > 0:
		positivos += nr
		contante += 1
		med = positivos/contante

print(contante,"valores positivos")
print("{:.1f}".format(med))