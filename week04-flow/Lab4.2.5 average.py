# Keeps reading numbers until the user enters a 0. (the program should append each of them into a list)
# The program should then print out each of the numbers entered and the average of them
# Author: Shane O'Gorman

num = int(input("Enter number (0 to quit): "))
arr = [] 

while num != 0: # Until 0 is entered each number is entered into the array. 
    arr.append(num)
    num = int(input("Enter number (0 to quit): "))
    
for value in arr: # Prints values in arr 
    print(value)

average = float(sum(arr))/len(arr) # Calculates the average of number in the array 
print(average)