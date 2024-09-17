N = int(input())

for x in range(0, N):
	X = int(input())

	if X == 0:
		print('NULL')

	elif X % 2 == 0:
		if X > 0:
			print('EVEN POSITIVE')
		elif X < 0:
			print('EVEN NEGATIVE')

	elif X % 2 != 0:
		if X > 0:
			print('ODD POSITIVE')
		elif X < 0:
			print('ODD NEGATIVE')
