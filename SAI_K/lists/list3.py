student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
lessthan_50=0
morethan_50=0
index=0
len=len(student_marks)
while index<len:
    if student_marks[index]<50:
        lessthan_50+=1
    else:
        morethan_50+=1
    index+=1
print("student marks less than 50 =",lessthan_50)
print("student marks greater than 50 =",morethan_50)
