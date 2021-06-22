import random
name = input("What is your name?---> ")
print("Good Luck ! ", name)
words =["variable","data types","operator","if-else","loops","list","set","tupple","dictionary","function","files"]
word = random.choice(words)
print("Guess the words:IT IS ABOUT OUR PYTHON SYLLABUS:::")
guesses = ''
turns = 10
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("*****You Won Congratulations*****")
        print("The word is: ", word)
        break
    guess = input("guess a character:")
    guesses += i
    if guess not in word:
        turns -= 1
        if turns==9:
            print("9 turns left")
            print("-----------")
        if turns==8:
            print("8 turns left")
            print("-----------")
            print("    O     ")
        if turns==7:
            print("7 turns left")
            print("-----------")
            print("    O     ")
            print("    |     ")
        if turns==6:
            print("6 turns left")
            print("-----------")
            print("    O     ")
            print("    |      ")
            print("   /        ")
        if turns==5:
            print("5 turns left")
            print("-----------")
            print("    O     ")
            print("    |      ")
            print("   / \      ")
        if turns==4:
            print("4 turns left")
            print("-----------")
            print("  \ O     ")
            print("    |      ")
            print("   / \     ")
        if turns==3:
            print("3 turns left")
            print("-----------")
            print("  \ O /    ")
            print("    |      ")
            print("   / \     ")
        if turns==2:
            print("2 turns left")
            print("-----------")
            print("  \ O / |    ")
            print("    |      ")
            print("   / \     ")
        if turns==1:
            print("1 turn left")
            print("-----------")
            print("      O_|    ")
            print("    / | \      ")
            print("     / \     ")
            
        if turns == 0:
            print("the word was:",word)
            print("You Loose") 
            break
