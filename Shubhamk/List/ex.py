question_list = [
    "1)How many continents are there?",        
    "2)What is the capital of India?",          
    "3)NG mei kaun se course padhaya jaata hai?" 
]
options_list = [
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution_list = [3, 4, 1] 
option=[["1 eight\n","3 seven"],["2 Bhopal\n","4 Delhi"],["1 Software Engineering\n","3 Tourism"]]
print("-----------WELCOME TO KBC-------------------")
i=0
count=0
sum=0
while(i<len(question_list)):
    j=0
    print("Your question is here---->")
    print(question_list[i])
    while(j<len(options_list[i])):
        print(j+1,options_list[i][j])
        j+=1
    answer=int(input("Enter your Answer--->"))
    if(answer == solution_list[i]):
        sum=sum+10000
        print("Congratulations Your Answer Is Right And You Have Won--->",sum)
    else:
        print("Your Answer Is Wrong You Lost---->",sum)
        print("----Game Over-----")
        break
    i+=1