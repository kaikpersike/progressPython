#Sequencia de lógica
x, y = input().split()
x = int(x)
y = int(y)

if 1<x<20 and x<y<100000:
    for i in range(1, y+1):
        if i%x!=0:
            print(i, end=" ")
        else:
            print(i)