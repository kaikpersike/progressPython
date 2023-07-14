#Médias ponderadas
N = int(input())
for i in range(N):
    
    a, b, c = input().split()
    a = float(a)
    b = float(b)
    c = float(c)
    calc = (a*2+b*3+c*5)/10 
    print(f"{calc:.1f}")