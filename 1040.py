nr = input().split()

n1 = float(nr[0])
n2 = float(nr[1])
n3 = float(nr[2])
n4 = float(nr[3])


media = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/((2)+(3)+(4)+(1))
print("Media: {:.1f}".format(media))


if media >= 7.0:
	print("Aluno aprovado.")

elif media >= 5.0 and media <= 6.9:
	print("Aluno em exame.")

	exame = float(input())

	print("Nota do exame: {:.1f}".format(exame))

	final = ((media)+(exame))/(2)
	
	if final >= 5.0:
		print("Aluno aprovado.")
	elif final <= 4.9:
		print("Aluno reprovado.")

	print("Media final: {:.1f}".format(final))

elif media <= 4.9:
	print("Aluno reprovado.")