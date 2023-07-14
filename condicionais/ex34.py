#Imposto de renda
salario = float(input())

if 0 <= salario <= 2000:
    print("Isento")
else:
    if 2000.01 <= salario <= 3000:
        isento = salario-2000
        ir = isento*0.08
        print(f"R$ {ir:.2f}")
    elif 3000.01<= salario <= 4500:
        isento = salario-2000
        ult = salario-3000
        ins = isento - ult
        aqui = ult*0.18
        dela = ins*0.08
        ir = aqui+dela
        print(f"R$ {ir:.2f}")
    elif salario>4500:
        isento = salario-2000
        ult = salario-4500
        ins = isento-ult
        prim = ins-1000
        seg = ins-prim
        soma1 = seg*0.08
        soma2 = prim*0.18
        soma3 = ult*0.28
        ir = soma1+soma2+soma3
        print(f"R$ {ir:.2f}")