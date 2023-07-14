# Aumento de salario
salario = float(input())
if 0 <= salario <= 400:
    reajuste = salario*0.15
    percentual = (reajuste*100)/salario
    print(f"Novo salario: {salario+reajuste:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {int(percentual)} %")
elif 400.01 <= salario <=800:
    reajuste = salario*0.12
    percentual = (reajuste*100)/salario
    print(f"Novo salario: {salario+reajuste:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {int(percentual)} %")
elif 800.01 <= salario <=1200:
    reajuste = salario*0.1
    percentual = (reajuste*100)/salario
    print(f"Novo salario: {salario+reajuste:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {int(percentual)} %")
elif 1200.01 <= salario <=2000:
    reajuste = salario*0.07
    percentual = (reajuste*100)/salario
    print(f"Novo salario: {salario+reajuste:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {int(percentual)} %")
else:
    reajuste = salario*0.04
    percentual = (reajuste*100)/salario
    print(f"Novo salario: {salario+reajuste:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {int(percentual)} %")