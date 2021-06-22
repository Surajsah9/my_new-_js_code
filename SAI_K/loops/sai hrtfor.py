n=int(input())
for r in range (n):
    for c in range (n):
        if (((r==0 or r==3) and (c%2!=0)) or (r==1 and (c%2==0)) or (r==2 and (c%4==0)) or (r==4 and (c==2))):
            print("s",end=" ")
        else:
            print(end="  ")
    print()