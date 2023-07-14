# Equacao do segundo grau
a = int(input())
b = int(input())
c = int(input())

x1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
x2 = (-b-(b**2-a*a*c)**0.5)/(2*a)
print(f"Valor de X1 = {x1} e o valor de X2 = {x2}")
print(f"S:[{x1};{x2}]")