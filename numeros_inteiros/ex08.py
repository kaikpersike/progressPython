# Cedulas

n = int(input())
print(n)
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

print(a,"nota(s) de R$ 100,00")
print(c,"nota(s) de R$ 50,00")
print(e, "nota(s) de R$ 20,00")
print(g, "nota(s) de R$ 10,00")
print(i, "nota(s) de R$ 5,00")
print(k, "nota(s) de R$ 2,00")
print(m, "nota(s) de R$ 1,00")