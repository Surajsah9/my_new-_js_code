#PALINDROME
a=int(input("En num:-"))
while len(str(a))!=2:
    b=a+a
    a=b
if len(str(a))>1:
    s=""
    b=a
    while a!=0:
        r=a%10
        s+=str(r)
        a=a//10
        if a==0:
            if b==int(s):
                print(b,"pal")
                break
            else:
                a=b+int(s)
                b=a
                s=""