# horas H:M:S
segundos = int(input()) #inserindo quantidade de segundos
t_min = segundos//60 #pegando os valores inteiros da divisão por segundos
t_seg = segundos%60 #pegando os valores restantes da divisão por segundos
t_hor = t_min//60 #pegando os valores inteiros da divisão por minutos
t_min = t_min%60 # pegando valores restantes da divisão por minutos. Está desconsiderando o valor t_min anterior, mas ele existe...
print(f"{t_hor}:{t_min}:{t_seg}")
