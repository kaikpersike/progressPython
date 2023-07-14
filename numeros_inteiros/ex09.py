# Conversao do tempo

segundos = int(input())
min = segundos//60
seg = segundos%60
hor = min//60
min = min%60
print(f"{hor}:{min}:{seg}")