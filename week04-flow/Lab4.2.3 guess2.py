# The program tells the user if there guess is too high or too low, each time they guess
# Author: Shane O'Gorman

num = int(input("Please guess the number: "))
rightNum = 30

while num != rightNum: # Until input number is input this will keep happening
    print("Wrong")
    if (num < rightNum): # Tells user whether their guess is to low or high
        print("Too Low")
    else:
        print("Too High")
    num = int(input("Please guess again: "))

print("Well done! Yes the number was ", rightNum)