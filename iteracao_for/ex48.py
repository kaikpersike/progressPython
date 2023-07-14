#Soma de impares consecutivos II
N = int(input())

for _ in range(N):
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    soma = 0
    if Y<X:
        X, Y = Y, X

    for i in range(X+1, Y):
        if i%2!=0:
            soma = soma+i
    print(soma)