minu = 0
hora = 0
segs = int(input())

if segs == 60:
	minu += 1
	segs = 0
	print("{}:{}:{}".format(hora,minu,segs))
	minu = 0
elif segs < 60:
	print("{}:{}:{}".format(hora,minu,segs))
elif segs > 60:
	while (segs-60)>= 0:
		segs -= 60
		minu += 1
		if minu >= 60:
			hora += 1
			minu = 0
	print("{}:{}:{}".format(hora,minu,segs))