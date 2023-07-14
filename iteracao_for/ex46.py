#Maior e posição
maior = 0
for i in range(5):
    n = int(input())
    if n>maior:
        maior = n
        cont = i+1
print(maior)
print(cont)
