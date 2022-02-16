# Create a program that puts 10 random numbers into a queue(list), the
# program should then output all the values in the queue, then take the
# numbers from the queue one at a time, print it and the current numbers still
# in the queue. (the command pop(0) takes the first element out of a list)

# Author: Shane O'Gorman

import random

originalQueue = [] 
lengthOfQueue = 10
upTo = 100

# Fills list with random integers between 0, 100
i = 0
while i < lengthOfQueue:
    originalQueue.append(random.randint(0,upTo))
    i+=1

print("queue is", originalQueue)

# Loop through the original list printing out the first number (that has been taken out using pop)
# And also print out the whole list 
j = 0
while j < lengthOfQueue:
    print("current Number is ", originalQueue.pop(0), "and the queue is", originalQueue)
    j+=1
print("the queue is now empty")
