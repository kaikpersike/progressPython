#Soma de impares consecutivos
X = int(input())
Y = int(input())
soma = 0
if Y<X:
    X, Y = Y, X

if X<0 or Y<0:
    for valor in range(X+1, Y+1):
        if valor%2!=0:
            soma = soma+valor
else:
    for valor in range(X, Y):
        if valor%2!=0:
            soma = soma+valor
print(soma)