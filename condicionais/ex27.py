# Media 3
n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
media  = (n1*2 + n2*3 + n3*4 + n4*1)/10

if media >= 7.0:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")
elif media<5:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")
elif 5 <= media <=6.9:
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    
    exame = float(input())
    print(f"Nota do exame: {exame:.1f}")
    rec = (media+exame)/2
    if rec>=5.0:
        print("Aluno aprovado.")
        print(f"Media final: {rec:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {rec:.1f}")