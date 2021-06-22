names=["sai","roshan","vishal","ranjan","ankit","shabid"]
ages=[23,23,20,22,21,22]
lenn=len(names)
lena=len(ages)
print(len(names))
print(len(ages))
n_a=[names,ages]
print(n_a)
print(len(n_a))
index=0
if lenn==lena:
    while index<lenn or lena:
        print(names[index],":",ages[index])
        index+=1
print()