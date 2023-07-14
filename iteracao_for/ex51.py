#Fibonacci facil
n = int(input())
if n == 1:
    print("0")
elif n == 2:
    print("0 1")
else:
    print("0 1", end=" ")
    a = 0
    b = 1
    
    for i in range (n-2):
        soma = a+b
        print(soma, end = " ")
        a = b
        b = soma
        