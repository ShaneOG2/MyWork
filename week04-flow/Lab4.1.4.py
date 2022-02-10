# Use a while loop to modify 1 so that it keeps prompting the user for a number until the user enters -1
# Author: Shane O'Gorman

num = -1
userNum = int(input("Enter a number "))
check = True 

while (check): # Until check changes from true to false run loop
    if (num == userNum): # If they enter -1 check changes to false
        check = False
        print("Got it!")
    else: # If not check remains as true and ask user to enter another number
        check = True
        userNum = int(input("Wrong! Enter a number: "))
