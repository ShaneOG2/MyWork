# The program tells the user if there guess is too high or too low, each time they guess
# Author: Shane O'Gorman

import random
rightNum = random.randint(0,100) #https://www.programiz.com/python-programming/examples/random-number

num = int(input("Please guess the number: "))

while num != rightNum: # Until input number is input this will keep happening
    print("Wrong")
    if (num < rightNum): # Tells user wheter their guess is to low or high
        print("Too Low")
    else:
        print("Too High")
    num = int(input("Please guess again: "))

print("Well done! Yes the number was ", rightNum)