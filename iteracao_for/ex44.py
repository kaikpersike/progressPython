#Resto 2
N = int(input())
if N<1000:
    for i in range(1, 10000):
        if i%N==2:
            print(i)