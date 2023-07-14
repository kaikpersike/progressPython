#Multiplos de 13
X = int(input())
Y = int(input())
if Y<X:
    X, Y = Y, X
soma = 0
for i in range(X, Y+1):
    if i%13!=0:
        soma = soma+i
print(soma)