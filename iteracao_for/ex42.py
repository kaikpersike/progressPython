#Intervalo 2
N = int(input())
ins = 0
out = 0
if N<10000:
    for i in range(N):
        X = int(input())
        if -10**7<=X<=10**7:
            if 10<=X<=20:
                ins = ins+1
            else:
                out = out+1
            
print(ins, "in")
print(out, "out")