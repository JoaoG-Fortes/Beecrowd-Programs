xy = input().split()

x = float(xy[0])
y = float(xy[1])


if x > 0.0 and y > 0.0:
	print("Q1")

elif x < 0.0 and y > 0.0:
	print("Q2")

elif x < 0.0 and y < 0.0:
	print("Q3")

elif x > 0.0 and y < 0.0:
	print("Q4")

elif x == 0.0 and y == 0.0:
	print("Origem")

elif x == 0.0 and y != 0.0:
	print("Eixo Y")

elif x != 0.0 and y == 0.0:
	print("Eixo X")