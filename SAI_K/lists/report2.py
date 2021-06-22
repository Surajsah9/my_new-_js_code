marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
] 
s=l=0
for r in range(len(marks)):
    s+=sum(marks[r])
    l+=len(marks[r])
print("total sum:-",s,"\n","average:-",s/l)
print()


marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
] 
sum=ts=0
for r in range(len(marks)):
    c=0
    while c<len(marks[r]):
        sum+=marks[r][c]
        c+=1
        ts+=1
print("total marks :-",sum)
print("average :-",sum/ts)
print()


marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]
] 
sum=ts=0
for r in range(len(marks)):
    c=0
    while c<len(marks[r]):
        sum+=marks[r][c]
        c+=1
        ts+=1
print("total marks :-",sum)
print("average :-",sum/ts)
print()
