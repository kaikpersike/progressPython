#Grenais
while True:
    x1, x2 = input().split()
    x1 = int(x1)
    x2 = int(x2)
    cont = 1

    inter = 0
    grem = 0
    emp = 0

    if x1 > x2:
        inter = 1
        grem = 0
    elif x2 > x1:
        grem = 1
        inter = 0

    if x1 == x2:
        emp = 1

    print("Novo grenal (1-sim 2-nao)")
    res = int(input())
    while res == 1:
        x1, x2 = input().split()
        x1 = int(x1)
        x2 = int(x2)
        print("Novo grenal (1-sim 2-nao)")
        res = int(input())
        cont+=1

        if x1 > x2:
            inter += 1
        elif x2 > x1:
            grem += 1

        if x1 == x2:
            emp+=1
    if res != 1:
        print (cont,"grenais")
        print(f"Inter:{inter}")
        print(f"Gremio:{grem}")
        print(f"Empates:{emp}")

        if inter > grem:
            print("Inter venceu mais")
        elif grem>inter:
            print("Gremio venceu mais")
        else:
            print("Nao houve vencedor")
        break