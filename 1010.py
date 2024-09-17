obj1 = input().split()
quant1 = int(obj1[1])
preco1 = float(obj1[2])

obj2 = input().split()
quant2 = int(obj2[1])
preco2 = float(obj2[2])

valor1 = quant1*preco1
valor2 = quant2*preco2

valortotal = valor1+valor2

print("VALOR A PAGAR: R$ {:.2f}".format(valortotal))