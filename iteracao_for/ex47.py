#Experiencia...
N = int(input())
somaCobaia = 0
somaCoelho = 0
somaRato = 0
somaSapo = 0
for i in range(N):
    quantia, tipo = input().split()
    quantia = int(quantia)
    tipo = str(tipo)
    if 1<=quantia<=15:
        somaCobaia = somaCobaia+quantia
    if tipo == "C" or tipo == "R" or tipo == "S":
        if tipo == "C":
            somaCoelho = somaCoelho+quantia
        elif tipo == "R":
            somaRato = somaRato+quantia
        else:
            somaSapo = somaSapo+quantia

print(f"Total: {somaCobaia} cobaias")
print(f"Total de coelhos: {somaCoelho}")
print(f"Total de ratos: {somaRato}")
print(f"Total de sapos: {somaSapo}")
percentualCoelho = (somaCoelho*100)/somaCobaia
percentualRato = (somaRato*100)/somaCobaia
percentualSapo = (somaSapo*100)/somaCobaia
print(f"Percentual de coelhos: {percentualCoelho:.2f} %")
print(f"Percentual de ratos: {percentualRato:.2f} %")
print(f"Percentual de sapos: {percentualSapo:.2f} %")
