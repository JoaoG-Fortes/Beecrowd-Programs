from math import*

pont1 = input().split()
pont2 = input().split()

x1 = float(pont1[0])
y1 = float(pont1[1])

x2 = float(pont2[0])
y2 = float(pont2[1])

distancia = sqrt(((x2-x1)**2)+((y2-y1)**2))

print("{:.4f}".format(distancia))