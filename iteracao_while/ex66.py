#Sequencia de numeros e soma
while True:
    m, n = input().split()
    m = int(m)
    n = int(n)
    maior = 0
    menor = 0
    soma = 0
    if m == 0 or n == 0 or m<0 or n<0:
        break
    if m>n:
        maior = m
        menor = n
    else:
        maior = n
        menor = m

    while menor<=maior:
        print(menor, end=" ")
        soma = soma+menor
        menor+=1
        
    print(f"Sum={soma}")