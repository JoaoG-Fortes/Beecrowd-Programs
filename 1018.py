N = int(input())
a = 'nota(s)'

div = N//100
cem = (N%100)
cinquenta = ((cem)//50)
vinte = ((cem)%50//20)
dez = ((cem)%50%20//10)
cinco = ((cem)%50%20%10//5)
dois = ((cem)%50%20%10%5//2)
um = ((cem)%50%20%10%5%2//1)

print("{}".format(N))
print("{} {} de R$ 100,00".format(div, a))
print("{} {} de R$ 50,00".format(cinquenta, a))
print("{} {} de R$ 20,00".format(vinte, a))
print("{} {} de R$ 10,00".format(dez, a))
print("{} {} de R$ 5,00".format(cinco, a))
print("{} {} de R$ 2,00".format(dois, a))
print("{} {} de R$ 1,00".format(um, a))