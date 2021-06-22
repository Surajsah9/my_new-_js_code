list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7] 
l_store=[]
for i in list1:
    if i not in list2:
        l_store.append(i)
print(l_store)
print()