#Quadrado de pares
N = int(input())
if 5<N<2000:
    for vl in range(1, N+1):
        if vl%2==0:
            print(f"{vl}^2 = {vl**2}")
