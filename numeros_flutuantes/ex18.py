# Areas
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

tri = (a*c)/2
print(f"TRIANGULO: {tri:.3f}")
cir = 3.14159*(c**2)
print(f"CIRCULO: {cir:.3f}")
tra = ((a+b)*c)/2
print(f"TRAPEZIO: {tra:.3f}")
qua = b*b
print(f"QUADRADO: {qua:.3f}")
ret = a*b
print(f"RETANGULO: {ret:.3f}")