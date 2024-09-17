dia_comeco = input().split()
horario_com = input().split(' : ')

dia_final = input().split()
horario_fim = input().split(' : ')

#data e hora de começo
dia_com = int(dia_comeco[1])
hora_com = int(horario_com[0])
min_com = int(horario_com[1])
seg_com = int(horario_com[2])

#data e hora de término
dia_fim = int(dia_final[1])
hora_fim = int(horario_fim[0])
min_fim = int(horario_fim[1])
seg_fim = int(horario_fim[2])

dias = dia_fim - dia_com
horas = hora_fim - hora_com
mins = min_fim - min_com
segs = seg_fim - seg_com

if segs < 0:
	mins -= 1
	segs += 60

if mins < 0:
	horas -= 1
	mins += 60

if horas < 0:
	dias -= 1
	horas += 24


print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{mins} minuto(s)')
print(f'{segs} segundo(s)')
