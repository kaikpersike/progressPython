# Triângulo
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
if b-c<a < b+c:
    per = a+b+c
    print(f"Perimetro = {per}")
else:
    area = ((a+b)*c)/2
    print(f"Area = {area}")