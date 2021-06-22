n=int(input())
r=0
while r<=n:
    c=0
    while c<=n:
        if (((r==0 or r==3) and (c%2!=0)) or (r==1 and (c%2==0)) or (r==2 and (c%4==0)) or (r==4 and (c==2))):
            print("s",end=" ")
        else:
            print(end="  ")
        c+=1
    print()
    r+=1