numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
index=count=0
while index<len(numbers):
    if numbers[index]>20 and numbers[index]<40:
        count+=1
    else:
        pass
    index+=1
print(count)
print()