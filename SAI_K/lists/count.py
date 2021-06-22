a=[1,1,2,2,3,3,4,5,5,6,6,6,7,7,8,8,9]
b=[i for i in a if a.count(i)>1]
print(b)
print()


a=[1,1,2,2,3,3,4,5,5,6,6,6,7,7,8,8,9]
b=[]
for i in a:
     if a.count(i)>1:
         b.append(i)
print(b)
print()


a=[1,1,2,2,3,3,4,5,5,6,6,6,7,7,8,8,9]
b=[i for i in a if a.count(i)<2]
print(b)
print()


a=[1,1,2,2,3,3,4,5,5,6,6,6,7,7,8,8,9]
b=[]
for i in a:
     if a.count(i)<2:
         b.append(i)
print(b)
print()
