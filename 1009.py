nome = input()
salfix = float(input())
vendas = float(input())

comissao = vendas*0.15

saltotal = salfix+comissao

print("TOTAL = R$ {:.2f}".format(saltotal))