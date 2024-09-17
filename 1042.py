lista = []
nrs = input().split()

n1 = int(nrs[0])
n2 = int(nrs[1])
n3 = int(nrs[2])

lista.append(n1)
lista.append(n2)
lista.append(n3)
lista.sort()

print("{}".format(lista[0]))
print("{}".format(lista[1]))
print("{}".format(lista[2]))
print("")
print("{}".format(n1))
print("{}".format(n2))
print("{}".format(n3))