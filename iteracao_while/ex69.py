#Sequencias crescentes
while True:
    x = int(input())
    while x!=0:
        i = 1
        while i <x+1:
            if i ==x:
                print(i)
            else:
                print(i, end=" ")

            i+=1
        break
    if x == 0:
        break