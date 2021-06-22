marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
#FOR loop
sum=0
for r in marks:
    for c in r:
        sum+=c
print(sum)
print()


#WHILE loop
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]
] 
r=sum=0
while r<len(marks):
    c=0
    while c<len(marks[r]):
        sum+=marks[r][c]
        c+=1
    r+=1
print(sum)
print()


#FOR and WHILE loop
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
]
sum=0
for r in range(0,len(marks)):
    c=0
    while c<len(marks[r]):
        sum+=marks[r][c]
        c+=1
    r+=1
print(sum)
print()


#FOR loop
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
]
s=0
for r in range(0,len(marks)):
    s+=sum(marks[r])
print(s)
print()


#FOR loop
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
]
s=[]
for r in range(0,len(marks)):
    s+=marks[r]
print(sum(s))