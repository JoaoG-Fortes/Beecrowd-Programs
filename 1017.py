temp_gasto = int(input())
vel_med = int(input())

combustivel = ((vel_med / 12)*temp_gasto)
print("{:.3f}".format(combustivel))