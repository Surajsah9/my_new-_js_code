print("palindrome example :- NITIN ")
print()


palindrome=str(input("Enter a palindrome string:-"))
l_palindrome=list(palindrome)
print(l_palindrome)
index=len(l_palindrome)-1
rl_palindrome=[]
while index>=0:
    rl_palindrome.append(l_palindrome[index])
    index-=1
print(rl_palindrome)
if l_palindrome==rl_palindrome:
    print(palindrome,":-it is a palindrome")
else:
    print(palindrome,":-it is not a palindrome")
print()


p=str(input("Enter a string palindrome:-"))
a=list(p)
print(p)
l=len(a)
b=[]
for i in range(l-1,-1,-1):
    b+=a[i]
print(b)
if a==b:
    print(p,":-it is a palindrome")
else:
    print(p,":-it is not a palindrome")
