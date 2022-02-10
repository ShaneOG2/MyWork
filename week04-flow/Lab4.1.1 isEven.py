# Asks the user to enter in a number, and the program will tell the user if the number is even or odd
# Author: Shane O'Gorman

num = int(input("Enter a number: "))

if (num % 2 == 0): # Checks if number is even
    print("{} is an even number".format(num))
else: # Otherwise its odd
    print("{} is an odd number".format(num))
