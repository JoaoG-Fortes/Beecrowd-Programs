dic = {'1':4.00, '2':4.50, '3':5.00, '4':2.00, '5':1.50}

lanche = input().split()

codigo = str(lanche[0])
quantidade = int(lanche[1])

a = quantidade * dic[codigo]
print("Total: R$ {:.2f}".format(a))