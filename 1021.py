N = float(input())
a = 'nota(s)'
b = 'moeda(s)'
nota = 'NOTAS:'
moeda = 'MOEDAS:'

#NOTAS
div = (N//100)
cem = (N%100)
cinquenta = ((cem)//50)
vinte = (((cem)%50)//20)
dez = ((((cem)%50)%20)//10)
cinco = (((((cem)%50)%20)%10)//5)
dois = ((((((cem)%50)%20)%10)%5)//2)

print("{}".format(nota))
print("{:.0f} {} de R$ 100.00".format(div, a))
print("{:.0f} {} de R$ 50.00".format(cinquenta, a))
print("{:.0f} {} de R$ 20.00".format(vinte, a))
print("{:.0f} {} de R$ 10.00".format(dez, a))
print("{:.0f} {} de R$ 5.00".format(cinco, a))
print("{:.0f} {} de R$ 2.00".format(dois, a))

#MOEDAS
div2 = ((((((cem)%50)%20)%10)%5)%2)
real = (div2//1)
cinqcent = ((div2%1)//0.50)
vintecent = (((div2%1)%0.50)//0.25)
dezcent = ((((div2%1)%0.50)%0.25)//0.10)
cincocent = (((((div2%1)%0.50)%0.25)%0.10)//0.05)
umcent = ((((((div2%1)%0.50)%0.25)%0.10)%0.05)/0.01)

print("{}".format(moeda))
print("{:.0f} {} de R$ 1.00".format(real, b))
print("{:.0f} {} de R$ 0.50".format(cinqcent, b))
print("{:.0f} {} de R$ 0.25".format(vintecent, b))
print("{:.0f} {} de R$ 0.10".format(dezcent, b))
print("{:.0f} {} de R$ 0.05".format(cincocent, b))
print("{:.0f} {} de R$ 0.01".format(umcent, b))