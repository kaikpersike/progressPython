# Idade em dias

n = int(input())

ano = n//365
mes = n%365
m = mes//30
dia = mes%30
print(ano,"ano(s)")
print(m,"mes(es)")
print(dia,"dia(s)")