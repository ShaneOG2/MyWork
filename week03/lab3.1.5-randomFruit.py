# Lab 3.1.5
# Prints out random fruit from fruit list 
# Author: Shane O'Gorman 

import random
fruits = ["Apple", "Orange", "Banana", "Pear"]

# Index is a random int between 0 and 3 (i.e lenght of list - 1)
index = random.randint(0, len(fruits)-1)
print("A Random Fruit: {}".format(fruits[index]))

