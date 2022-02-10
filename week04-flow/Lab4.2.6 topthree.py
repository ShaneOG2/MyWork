# Write a program (topthree.py) generates 10 random numbers (0-100) ,prints them out then prints out the top three. 
# Author: Shane O'Gorman

import random

arr = []
i = 0
while i < 10:
    arr.append(random.randint(0,100))
    i += 1
print(arr)

# https://stackoverflow.com/q/32296887
# Copies original list, sorts it highest to lowest then returns the first 3 i.e. the top 3
topOnes = arr.copy()
topOnes.sort(reverse = True)
print ("The top {} are \t\t {}".format(3,topOnes[0:3]))
