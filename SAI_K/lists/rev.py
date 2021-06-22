#LIST
capitals=["hyderabad","mumbai","kolkata","delhi"]
capitals.reverse()
print(capitals)
print()

#FOR
capitals=["hyderabad","mumbai","kolkata","delhi"]
r_capitals=[]
for index in range(len(capitals)-1,-1,-1):
    r_capitals.append(capitals[index])
print(r_capitals)
print()


#WHILE
capitals=["hyderabad","mumbai","kolkata","delhi"]
r_capitals=[]
index=len(capitals)-1
while 0<=index:
    r_capitals.append(capitals[index])
    index-=1
print(r_capitals)

