flag = True

while flag==True:
	try:
		L = int(input())
		V = input().split()

		int_V = list(map(int, V))

		if max(int_V) < 10:
			print("1")

		elif max(int_V) >= 10 and max(int_V) < 20:
			print("2")

		else:
			print("3")

	except EOFError:
		flag = False
	except ValueError:
		flag = False
