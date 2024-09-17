numeros = input().split()

a = int(numeros[0])
b = int(numeros[1])
c = int(numeros[2])

maior1 = (a+b+abs(a-b))/2
maior2 = (maior1+c+abs(maior1-c))/2
print("{:.0f} eh o maior".format(maior2))