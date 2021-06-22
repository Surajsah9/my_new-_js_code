n=int(input())
i=1
j=2*n
b=""
a=''
while i<=n or n<j:
    if i<=n:
        a+=str(i)
        i+=1
    else:
        b+=str(j)
        j-=1
print(a,"\n",b)


