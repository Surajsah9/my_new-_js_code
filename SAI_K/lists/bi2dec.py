#Binary to Decimal

binary=[1,0,0,1,1,0,1,1]
binary.reverse()
sum=power=0
for num in binary:
    sum+=num*2**power
    power+=1
print(sum)
print()



binary=[1,0,0,1,1,0,1,1]
sum=power=0
index=len(binary)-1
while 0<=index:
    sum+=binary[index]*2**power
    power+=1
    index-=1
print(sum)
