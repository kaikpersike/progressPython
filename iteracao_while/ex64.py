#Tipo de combustivel
cod = int(input())
alc = 0
gas = 0
die = 0
while cod>0:
    cod = int(input())
    if cod==1:
        alc = alc+1
    elif cod==2:
        gas = gas+1
    elif cod == 3:
        die = die+1
    if cod == 4:
        break

print("MUITO OBRIGADO")
print("Alcool:", alc)
print("Gasolina:", gas)
print("Diesel:", die)