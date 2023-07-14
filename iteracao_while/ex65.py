#Numeros pares e sequencia
while 1>0:
    x = int(input())
    stop = x+10
    soma=0
    if x==0:
        break
    while x<stop:
        if x%2==0:
            soma = soma+x
        x+=1
    print(soma)