true = True

while true==True:
	try:
		v, t = list(map(int, input().split()))

		deslocamento = v * (2*t)

		print(deslocamento)

	except ValueError:
		true = False
	except EOFError:
		true = False
