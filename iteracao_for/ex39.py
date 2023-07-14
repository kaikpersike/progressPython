#Numeros impares
X = int(input())
if 1<=X<=1000:
    for vl in range(X+1):
        if vl%2!=0:
            print(vl)