#Varias notas com validacao
while True:
    n1 = float(input())
    
    while n1 <0 or n1 >10:
        print("nota invalida")
        n1 = float(input())
    
    n2 = float(input())
    while n2 <0 or n2>10:
        print("nota invalida")
        n2 = float(input())

    print(f"media = {((n1+n2)/2):.2f}")
    print("novo calculo (1-sim 2-nao)")
    novo = int(input())
    while novo != 1 and novo !=2:
        print("novo calculo (1-sim 2-nao)")
        novo = int(input())

    if novo == 2:
        break