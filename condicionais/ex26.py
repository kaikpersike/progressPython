# Lanche
cod, num = input().split()
cod = int(cod)
num = int(num)

if cod == 1:
    print(f"Total: R$ {(num*4.00):.2f}")
elif cod == 2:
    print(f"Total: R$ {(num*4.50):.2f}")
elif cod == 3:
    print(f"Total: R$ {(num*5.00):.2f}")
elif cod == 4:
    print(f"Total: R$ {(num*2.00):.2f}")
elif cod == 5:
    print(f"Total: R$ {(num*1.50):.2f}")