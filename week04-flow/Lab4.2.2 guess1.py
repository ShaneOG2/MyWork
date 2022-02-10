# Prompts the user to guess a number, the program should keep prompting the user to guess the number until the user gets the right one
# Author: Shane O'Gorman

num = int(input("Please guess the number: "))
rightNum = 30

while num != rightNum: # Until input number is the right number this will keep happening
    print("Wrong")
    num = int(input("Please guess again: "))

print("Well done! Yes the number was ", rightNum)