# Notas e moedas
n = float(input())
a = n//100
b = n%100
c = b//50
d = b%50
e = d//20
f = d%20
g = f//10
h = f%10
i = h//5
j = h%5
k = j//2
l = j%2
m = l//1
n = l%1
o = n//(0.5)
p = n%(0.50)
q = p//(0.25)
r = p%(0.25)
s = r//(0.10)
t = r%(0.10)
u = t//(0.05)
v = t%(0.05)
w = (round(v*100)/100)/(0.01)

print("NOTAS:")
print(f"{a:.0f} nota(s) de R$ 100.00")
print(f"{c:.0f} nota(s) de R$ 50.00")
print(f"{e:.0f} nota(s) de R$ 20.00")
print(f"{g:.0f} nota(s) de R$ 10.00")
print(f"{i:.0f} nota(s) de R$ 5.00")
print(f"{k:.0f} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{m:.0f} moeda(s) de R$ 1.00")
print(f"{o:.0f} moeda(s) de R$ 0.50")
print(f"{q:.0f} moeda(s) de R$ 0.25")
print(f"{s:.0f} moeda(s) de R$ 0.10")
print(f"{u:.0f} moeda(s) de R$ 0.05")
print(f"{w:.0f} moeda(s) de R$ 0.01")