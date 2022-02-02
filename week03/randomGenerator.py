# Lab3.1.4
# Prints random number between the range of two int read 
# Author: Shane O'Gorman 

import random

x = int(input("Enter the range between two numbers you want a random number between: "))
y = int(input(""))
num = random.randint(x,y)

print("Here is a random number between {} and {}: {}".format(x, y, num))