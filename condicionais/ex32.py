# Tempo de jogo
inicio, fim = input().split()
inicio = int(inicio)
fim = int(fim)

if inicio > fim or inicio == fim:
    calc = (24-inicio)+fim
    print(f"O JOGO DUROU {calc} HORA(S)")
else:
    calc = fim-inicio
    print(f"O JOGO DUROU {calc} HORA(S)")