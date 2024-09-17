a = int(input())
lista = []

b = input().split()

for x in b:
	a = x
	x = list(x)
	x = x[::-1]
	x.remove(x[0])
	x = x[::-1]

	if "".join(x)== "OB" or "".join(x) == "UR":

		if "".join(x) == "OB":
			lista.append("OBI")
		else:
			lista.append("Beecrowd")

	else:
		lista.append(a)

print(str(lista[0:len(lista)]).replace("[", "").replace(",", "").replace("]", "").replace("'", ""))
