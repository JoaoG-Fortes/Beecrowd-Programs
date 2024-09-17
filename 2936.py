curupira = 300
boitata = 1500
boto = 600
mapinguari = 1000
iara = 150
chica = 225

porcoes = []

for x in range(0, 5):
	num = (int(input()))
	porcoes.append(num)

cur = porcoes[0]
boi = porcoes[1]
bot = porcoes[2]
mapi = porcoes[3]
iar = porcoes[4]

total = ((curupira*cur) + (boitata*boi) + (boto*bot) + (mapinguari*mapi) + (iara*iar) + chica)
print (total)
