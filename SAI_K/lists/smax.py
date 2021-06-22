numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
numbers.sort()
print("second maximum:-",numbers[-2])
print("second mimimun:-",numbers[1])
print()


numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
max=s_max=0
for item in numbers:
    if max<item:
        max=item
        for items in numbers:
            if max>items and items>s_max:
                s_max=items
print(s_max)
print()



numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
max=s_max=0
index=0
while index<len(numbers):
    if max<numbers[index]:
        max=numbers[index]
    index+=1
    index2=0
    while index2<len(numbers):
        if max>numbers[index2] and numbers[index2]>s_max:
            s_max=numbers[index2]
        index2+=1
print(s_max)
    

