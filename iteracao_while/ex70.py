#Idades
while True:
    x = int(input())
    cont = 1
    soma = x
    while x>0:
        x = int(input())
        if x>0:
            soma = soma +x
            cont +=1
    if x <0:
        print(f"{(soma/cont):.2f}")
        break
