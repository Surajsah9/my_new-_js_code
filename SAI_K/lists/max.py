numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
print(max(numbers))
print(min(numbers))
print()


numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
numbers.sort()
print("maximum number is:-",numbers[-1])
print("minimum number is:-",numbers[0])
print()


numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
max=0
for num in numbers:
    if max<num:
        max=num
print("max number is:-",max)
print()



numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
max=index=0
while index<len(numbers):
    if numbers[index]>max:
        max=numbers[index]
    index+=1
print(max)
print()



numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
index=0
min=numbers[0]
while index<len(numbers):
    if min>numbers[index]:
        min=numbers[index]
    index+=1
print(min)
print()



numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
print(sum(numbers))
print()


numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
index=sum=0 
while index<len(numbers):
    sum+=numbers[index]
    index+=1
print(sum)
print()


numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
sum=0
for item in numbers:
    sum+=item
print(sum)
print()