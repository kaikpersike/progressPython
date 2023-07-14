#Sequencia IJ 3
i = 1
j = 0
while i<10:
    if i%2!=0:
        if i ==1:
            j = j +7
            while j>4:
                print(f"I={i} J={j}")
                j-=1
        if i == 3:
            j = j+5
            while j>6:
                print(f"I={i} J={j}")
                j-=1
        if i == 5:
            j = j+5
            while j>8:
                print(f"I={i} J={j}")
                j-=1
        if i == 7:
            j = j+5
            while j>10:
                print(f"I={i} J={j}")
                j-=1
        if i ==9:
            j = j+5
            while j>12:
                print(f"I={i} J={j}")
                j-=1
    i +=1
    # 7,6,5,9,8,7,11,10,9,13,12,11,15,14,13