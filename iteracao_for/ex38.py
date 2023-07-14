#Par/ impar/ positivo/ negativo quantidade
par = 0
imp = 0
pos = 0
neg = 0
for valor in range(5):
    n = int(input())
    if n%2==0:
        par = par+1
    else:
        imp = imp+1
    if n>0:
        pos = pos+1
    elif n<0:
        neg = neg+1

print(par, "valor(es) par(es)")
print(imp, "valor(es) impar(es)")
print(pos, "valor(es) positivo(s)")
print(neg, "valor(es) negativo(s)")