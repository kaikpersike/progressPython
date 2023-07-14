#Tipos de triangulos
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

A = 0
B = 0
C = 0

if a > b and a > c:
    if b > c:
        A = a
        B = b
        C = c
    else:
        A = a
        B = c
        C = b
elif b > a and b > c:
    if a > c:
        A = b
        B = a
        C = c
    else:
        A = b
        B = c
        C = a
else:
    if a > b:
        A = c
        B = a
        C = b
    else:
        A = c
        B = b
        C = a


if A >= B+C:
    print("NAO FORMA TRIANGULO")
else:
    if A**2==B**2+C**2:
        print("TRIANGULO RETANGULO")
    elif A**2>B**2+C**2:
        print("TRIANGULO OBTUSANGULO")
    elif A**2<B**2+C**2:
        print("TRIANGULO ACUTANGULO")
    
    if A==B and A==C and B==C:
        print("TRIANGULO EQUILATERO")
    elif B==C or A==B:
        print("TRIANGULO ISOSCELES")